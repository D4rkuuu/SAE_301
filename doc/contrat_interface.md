# Contrat d'Interface DEV <-> DATA

**Version :** v1.9 | **Date :** 25/11/2026

Ce document définit le format et les règles d'échange de données entre le module **DEV** (récupération météo via API Open-Meteo et affichage web) et le module **DATA** (référentiels, calculs agronomiques et stockage en base de données).

## 0. Référentiels partagés (Source de vérité : BDD DATA)

Afin d'assurer la cohérence des clés étrangères entre le formulaire web (DEV) et la table `Fact_Indicateur` (DATA), les deux pôles s'appuient sur les tables de dimensions définies dans le schéma relationnel.

### Horizons climatiques (`Dim_Horizon`)

Chaque horizon couvre une **décennie complète de 10 ans** (sans chevauchement), intégralement disponible sur les deux modèles climatiques retenus (qui s'étendent jusqu'au `31/12/2049`).

| `id_horizon` | `label` | `annee_debut` | `annee_fin` | Plage API Open-Meteo |
| :---: | :---: | :---: | :---: | :---: |
| **1** | `2020-2029` | `2020` | `2029` | `2019-08-01` au `2029-12-31` |
| **2** | `2030-2039` | `2030` | `2039` | `2029-08-01` au `2039-12-31` |
| **3** | `2040-2049` | `2040` | `2049` | `2039-08-01` au `2049-12-31` |

*(DEV démarre systématiquement la requête au `01/08` de `annee_debut - 1` afin de couvrir les cultures d'hiver — colza dès le 20/08 N−1 et blé tendre dès le 15/10 N−1 — et garantir 10 campagnes complètes par horizon.)*

### Modèles climatiques (`Dim_Modele`)

| `id_modele` | `nom_modele` (code API Open-Meteo) | `organisme` |
| :---: | :--- | :--- |
| **1** | `MRI_AGCM3_2_S` | MRI (Meteorological Research Institute) |
| **2** | `EC_Earth3P_HR` | EC-Earth Consortium |

*(L'utilisateur final ne choisit pas le modèle dans l'interface : DEV interroge systématiquement les deux modèles en arrière-plan.)*

### Communes et cultures (`Dim_Commune`, `Dim_Culture`)

* **`Dim_Commune`** (`code_insee`, `nom`, `latitude`, `longitude`, `altitude_m`, `zone_climatique`) : utilisée par DEV pour alimenter le menu déroulant des communes et la résolution automatique des coordonnées GPS envoyées à Open-Meteo.
* **`Dim_Culture`** (`id_culture`, `nom`, `t_base_c`, `gdd_maturite_cj`, `seuil_gel_c`, `besoin_eau_mm`, `seuil_stress_c`, `t_opt_min_c`, `t_opt_max_c`) : utilisée par DEV pour alimenter le menu déroulant des cultures, et par DATA pour appliquer les seuils agronomiques.

## 1. Ce que DEV fournit à DATA (Entrée : Les Séries Climatiques)

**Rôle et fonctionnement :**

1. Pour une analyse demandée par l'utilisateur (`code_insee`, `id_culture`, `id_horizon`), le pôle DEV lit les coordonnées dans `Dim_Commune` et les bornes de la décennie dans `Dim_Horizon` (requête étendue au 01/08 de `annee_debut - 1`), puis effectue **un seul appel HTTP** vers l'API Open-Meteo Climate en demandant simultanément les deux modèles (`models=MRI_AGCM3_2_S,EC_Earth3P_HR`).
2. Ces séries journalières brutes ne sont **jamais stockées** en base de données (elles transitent uniquement en mémoire vive).
3. En mémoire, DEV découpe la réponse API et transmet au pipeline de calcul DATA **un objet formaté par modèle climatique** (soit 2 appels de fonction Python pour une analyse : un pour `MRI_AGCM3_2_S`, puis un pour `EC_Earth3P_HR`).

**Structure exacte d'un objet envoyé par DEV à DATA (pour 1 modèle) :**

```json
{
  "metadonnees": {
    "code_insee": "21231",          // FK Dim_Commune
    "nom_commune": "Dijon",         // Dim_Commune.nom (pour affichage IHM)
    "latitude": 47.32,              // Dim_Commune.latitude (utilisee pour la requete API)
    "longitude": 5.04,              // Dim_Commune.longitude
    "id_culture": 1,                // FK Dim_Culture (ex: 1 = ble tendre)
    "id_horizon": 3,                // FK Dim_Horizon (ex: 3 = 2040-2049)
    "horizon": "2040-2049",         // Dim_Horizon.label (periode projetee de 10 ans)
    "nom_modele": "MRI_AGCM3_2_S",  // Dim_Modele.nom_modele concerne par cette serie
    "id_session": "a3f9c2e1-7b4d"   // VARCHAR(64) : Cle technique de session anonyme generee par DEV
  },
  "series_meteo": [
    {
      "date": "2039-08-01",         // Date au format AAAA-MM-JJ (debut au 01/08 de annee_debut - 1)
      "t_min": 16.2,                // Temperature minimale du jour (degC) -> GEL et MATURITE (GDD)
      "t_max": 28.4,                // Temperature maximale du jour (degC) -> STRESS THERMIQUE et MATURITE (GDD, plafonnee a 30 degC pour le mais)
      "t_moy": 22.3,                // Temperature moyenne du jour (degC) -> Controle Hargreaves (ET0) et courbe mensuelle IHM
      "precip": 0.0,                // Cumul des precipitations (mm) -> BILAN HYDRIQUE
      "et0": 4.8                    // Evapotranspiration FAO (mm, champ API et0_fao_evapotranspiration_sum) -> Trace et controle (bilan hydrique calcule via Hargreaves en Sprint 1)
    }
    // ... (3 805 a 3 806 jours : du 01/08 de annee_debut - 1 au 31/12 de annee_fin)
  ]
}
```

## 2. Ce que DATA fournit à DEV (Sortie : Les Faits Stockés)

**Rôle :**
Pour chaque objet reçu (un modèle climatique), le pipeline de calcul DATA :

* croise `series_meteo` avec les seuils de `Dim_Culture` (`id_culture`),
* calcule chaque indicateur **année par année** sur la fenêtre sensible, puis effectue la **moyenne sur les 10 années** de l'horizon,
* stocke la ligne agrégée dans `Fact_Indicateur` (1 ligne par modèle via `id_modele`, identifiée par `id_fait`).

DEV interroge ensuite `Fact_Indicateur` (ou une vue/fonction mise à disposition par DATA) pour le quadruplet `(code_insee, id_culture, id_horizon, id_session)` et récupère une **liste de 2 objets** (un par modèle climatique) :

```json
[
  {
    "metadonnees_jointure": {
      "id_fait": 101,                 // PK Fact_Indicateur
      "code_insee": "21231",          // FK Dim_Commune
      "id_culture": 1,                // FK Dim_Culture (ex: 1 = ble tendre)
      "id_horizon": 3,                // FK Dim_Horizon (ex: 3 = 2040-2049)
      "id_modele": 1,                 // FK Dim_Modele (1 = MRI_AGCM3_2_S)
      "nom_modele": "MRI_AGCM3_2_S",  // Dim_Modele.nom_modele (via jointure)
      "id_session": "a3f9c2e1-7b4d"   // VARCHAR(64) : Cle technique de session anonyme
    },
    "indicateurs_calcules": {
      "gdd_cumul_moyen": 2230.0,      // DECIMAL(7,1) : somme thermique annuelle moyenne sur 10 ans via (t_min + t_max)/2 - t_base (t_max plafonnee a 30 degC pour le mais)
      "nb_jours_gel": 0.4,            // DECIMAL(4,1) : nombre moyen de jours de gel critique/an (fenetre sensible)
      "nb_jours_stress_th": 3.2,      // DECIMAL(4,1) : nombre moyen de jours de stress thermique/an (fenetre sensible)
      "bilan_hydrique_mm": -120.0     // DECIMAL(6,1) : bilan net moyen Precipitations - ET0 Hargreaves (mm, car et0 API surestimait)
    },
    "verdict": "A_RISQUE"             // VARCHAR(20) : VIABLE | A_RISQUE | NON_VIABLE
  },
  {
    "metadonnees_jointure": {
      "id_fait": 102,
      "code_insee": "21231",
      "id_culture": 1,
      "id_horizon": 3,
      "id_modele": 2,                 // FK Dim_Modele (2 = EC_Earth3P_HR)
      "nom_modele": "EC_Earth3P_HR",
      "id_session": "a3f9c2e1-7b4d"
    },
    "indicateurs_calcules": {
      "gdd_cumul_moyen": 2310.0,
      "nb_jours_gel": 0.2,
      "nb_jours_stress_th": 4.1,
      "bilan_hydrique_mm": -150.0
    },
    "verdict": "A_RISQUE"
  }
]
```

## 3. Synthèse multi-modèles et incertitude (DEV)

À partir des deux objets retournés par DATA ($v_1$ pour `MRI_AGCM3_2_S` et $v_2$ pour `EC_Earth3P_HR`), le contrôleur Flask calcule pour l'affichage dans les cartes KPI :

* **Valeur centrale (moyenne) :** $\frac{v_1 + v_2}{2}$
* **Marge d'incertitude :** $\pm \frac{|v_1 - v_2|}{2}$ (et fourchette $[\min(v_1, v_2), \max(v_1, v_2)]$)
* **Verdict global affiché :** principe de précaution en cas de divergence entre les deux modèles (`NON_VIABLE` > `A_RISQUE` > `VIABLE`), accompagné d'une mention signalant la divergence.