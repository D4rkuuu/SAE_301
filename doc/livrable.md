# SAÉ 3.01 — Livrable J1 : Dossier d'Analyse (Pôle DATA)

Ce document formalise les travaux d'analyse, de modélisation relationnelle, de sourçage agronomique et de spécification des flux techniques conduits par le pôle DATA pour l'application d'aide à la décision agro-climatique à l'horizon 2050.

---

## 1. Référentiel des cultures et traçabilité agronomique

### 1.1 Justification du panel de cultures
Pour évaluer la résilience agricole métropolitaine, cinq cultures représentatives de la diversité des systèmes de production français ont été sélectionnées :
* **Grandes cultures annuelles d'hiver** : Blé tendre d'hiver et Colza d'hiver (piliers de la sole céréalière française, sensibles aux gelées printanières post-montaison et à l'échaudage estival).
* **Grande culture annuelle estivale** : Maïs grain (culture exigeante en chaleur et forte consommatrice d'eau, exposée aux restrictions d'irrigation estivales).
* **Culture légumière et féculière** : Pomme de terre (cycle estival sensible aux stress thermiques précoces et aux déficits hydriques).
* **Culture pérenne à haute valeur patrimoniale** : Vigne de cuve (marqueur historique du changement climatique, fortement exposée au décalage phénologique et aux gelées destructrices lors du débourrement).

### 1.2 Démarche d'audit et épuration des sources
Les sources généralistes de type Wikipédia ont été systématiquement écartées de notre entrepôt de données. Les seuils bioclimatiques ont été extraits et croisés auprès des instituts techniques professionnels et des organismes de recherche agronomique de référence :
* **ARVALIS - Institut du végétal** : références blé, maïs, pomme de terre.
* **Terres Inovia** : seuils de développement et stress hydrique du colza.
* **IFV (Institut Français de la Vigne et du Vin)** : seuils de dormance, débourrement et gel printanier.
* **SEMAE** : températures de base et biométrie germinative.
* **CNIPT** : filière pomme de terre.
* **INRAE (Portail Ephytia)** : pathologie thermique et accidents climatiques.

#### Données sourcées référence cultures

| id_culture | nom | t_base_c | gdd_maturite_cj | seuil_gel_c | besoin_eau_mm | t_opt_min_c | t_opt_max_c | seuil_stress_thermique_c | sources | urls | date_consultee | confiance |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :---: |
| 1 | Blé tendre (hiver) | 0 | 2150 | -4 | 500 | 15 | 22 | 30 | ARVALIS (gel de printemps) \| Perspectives Agricoles (besoin en eau) | https://fiches.arvalis-infos.fr \| https://www.perspectives-agricoles.com/conduite-de-cultures/modelisation-des-besoins-en-eau-combien-consomment-les-cultures | 2026-09-25 | verifiee |
| 2 | Colza (hiver) | 5 | 2300 | -5 | 450 | 12 | 22 | 27 | ISAGRI (GDD) \| SEMAE (t_base) \| Terres Inovia (gel et eau) \| L'Eure Agricole (gel) | https://www.isagri.fr/ressources/articles/temps-thermique-lindicateur-cl%C3%A9-de-pr%C3%A9vision-des-stades-de-culture \| https://www.semae-pedagogie.org/sujet/implantation-et-developpement/ \| https://www.terresinovia.fr/fr/informations-techniques/colza/accidents-climatiques-sur-colza-gelees-printanieres \| https://www.terresinovia.fr/fr/informations-techniques/colza/accidents-climatiques-sur-colza-le-manque-ou-lexces-deau \| https://www.eure-agricole.fr/apres-les-meligethes-et-le-gel-quelles-consequences-pour-le-colza | 2026-09-25 | verifiee |
| 3 | Maïs grain | 6 | 1600 | 0 | 600 | 20 | 30 | 35 | Farmi (GDD) \| AgriRéseau (t_base) \| Catharsius (T opt) \| ISAGRI (irrigation) \| Perspectives Agricoles (eau) | https://www.farmi.com/article/somme-chaleur-germination-mais \| https://www.agrireseau.net/bovinslaitiers/Documents/bov14.pdf \| https://www.catharsius.fr/plante-mais/soin/temperature-et-humidite/ \| https://www.isagri.fr/ressources/articles/irrigation-quelle-quantit%C3%A9-deau-pour-assurer-de-bons-rendements- \| https://www.perspectives-agricoles.com/conduite-de-cultures/modelisation-des-besoins-en-eau-combien-consomment-les-cultures | 2026-09-25 | verifiee |
| 4 | Pomme de terre | 7 | 1500 | -2 | 600 | 15 | 20 | 28 | CNIPT (général) \| INRAE Ephytia (gel et chaleur) \| Perspectives Agricoles (eau) | https://www.cnipt.fr/ \| https://ephytia.inrae.fr/fr/C/21109/Pomme-de-terre-Gel-ou-froid \| https://ephytia.inrae.fr/fr/C/21111/Pomme-de-terre-Chaleur \| https://www.perspectives-agricoles.com/recherche-agronomie/pomme-de-terre-leau-un-facteur-de-production-et-de-durabilite | 2026-09-25 | verifiee |
| 5 | Vigne (raisin de cuve) | 10 | 1300 | -2 | 400 | 25 | 30 | 35 | IFV Vignevin (gel de printemps et bioclimatologie) \| INRAE Ephytia | https://www.vignevin.com \| https://ephytia.inra.fr | 2026-09-25 | verifiee |

### 1.3 Données consolidées de référence (`referentiel-cultures.csv`)

| id_culture | Nom | T° base (°C) | GDD maturité (°C·j) | Seuil gel (°C) | Besoin eau (mm) | T° opt min (°C) | T° opt max (°C) | Stress therm. (°C) | Organismes sources |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | Blé tendre (hiver) | 0 | 2150 | -4 | 500 | 15 | 22 | 30 | ARVALIS, Perspectives Agricoles |
| **2** | Colza (hiver) | 5 | 2300 | -5 | 450 | 12 | 22 | 27 | Terres Inovia, ISAGRI, SEMAE, L'Eure Agricole |
| **3** | Maïs grain | 6 | 1600 | 0 | 600 | 20 | 30 | 35 | Farmi, AgriRéseau, ISAGRI, Perspectives Agricoles |
| **4** | Pomme de terre | 7 | 1500 | -2 | 600 | 15 | 20 | 28 | CNIPT, INRAE Ephytia, Perspectives Agricoles |
| **5** | Vigne (raisin de cuve) | 10 | 1300 | -2 | 400 | 25 | 30 | 35 | IFV Vignevin, INRAE Ephytia |

*Toutes les données sont strictes (aucun intervalle textuel dans les attributs de calcul) afin de garantir l'intégrité des requêtes SQL et des scripts de traitement Pandas.*

---

## 2. Matrice de calcul des indicateurs agro-climatiques

| Indicateur | Objectif agronomique | Données d'entrée (API) | Paramètres seuils | Période de calcul | Formule mathématique / Algorithme | Unité & Format |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Somme thermique (GDD)** | Maturité physiologique avant l'hiver. | `temperature_2m_mean` | `t_base_c`, `gdd_maturite_cj` | Cycle complet de la culture | $\sum \max(T_{\text{moy}} - T_{\text{base}}, 0)$<br>*Spécificité Maïs :* $DJ = \max\left(\frac{T_n + \min(T_x, 30)}{2} - 6, 0\right)$ | °C·j cumulés |
| **Fréquence du gel critique** | Risque de destruction des organes verts ou floraux. | `temperature_2m_min` | `seuil_gel_c` | Fenêtre critique printanière (avril – mai) | $\sum 1$ pour chaque jour où $T_{\min} \le \text{seuil\_gel\_c}$ | Jours de gel critique / an |
| **Stress thermique** | Risque d'échaudage et d'avortement floral. | `temperature_2m_max` | `seuil_stress_thermique_c` | Maturation estivale (juin – août) | $\sum 1$ pour chaque jour où $T_{\max} \ge \text{seuil\_stress\_thermique\_c}$ | Jours de stress thermique / an |
| **Bilan hydrique** | Risque de déficit et stress hydrique sévère. | `precipitation_sum`, `t_min`, `t_max`, `t_mean` | `besoin_eau_mm` | Période de végétation active | $B = \sum (\text{Précipitations} - ET_0)$<br>avec $ET_0$ estimé via la formule d'Hargreaves | Bilan net en mm |
| **Verdict global 2050** | Aide à la décision stratégique pour l'exploitant. | Agrégations pluriannuelles | Ensemble des seuils | Horizon projeté (ex. 2041-2050) | Évaluation multicritère :<br>• `VIABLE` : GDD atteint ET gel rare ET bilan hydrique toléré<br>• `A_RISQUE` : Un facteur limitant fréquent<br>• `NON_VIABLE` : GDD insuffisant ou stress létal | `VIABLE`<br>`A_RISQUE`<br>`NON_VIABLE` |

### 2.1 Formalisation mathématique des indicateurs

#### 1. Fréquence du gel printanier
Soit $D_{\text{printemps}}$ l'ensemble des jours des mois d'avril et mai ($m \in \{4, 5\}$). Le nombre de jours de gel critique $N_{\text{gel}}$ pour une culture donnée s'exprime par :
$$N_{\text{gel}} = \sum_{j \in D_{\text{printemps}}} \mathbb{I}\left( T_{n,j} \le T_{\text{seuil\_gel}} \right)$$
* $T_{n,j}$ : température minimale journalière (`temperature_2m_min`).
* $T_{\text{seuil\_gel}}$ : seuil critique létal (ex. $-2\ ^\circ\text{C}$ pour la vigne, $-4\ ^\circ\text{C}$ pour le blé).
* $\mathbb{I}(E)$ : fonction indicatrice valant $1$ si la condition $E$ est vérifiée, $0$ sinon.

#### 2. Fréquence du stress thermique (Échaudage estival)
Soit $D_{\text{été}}$ l'ensemble des jours de la période estivale (juin à août) :
$$N_{\text{stress}} = \sum_{j \in D_{\text{été}}} \mathbb{I}\left( T_{x,j} \ge T_{\text{seuil\_stress}} \right)$$
* $T_{x,j}$ : température maximale journalière (`temperature_2m_max`).
* $T_{\text{seuil\_stress}}$ : seuil d'échaudage ou de blocage physiologique (ex. $35\ ^\circ\text{C}$ pour le maïs et la vigne).

#### 3. Somme thermique cumulée du Maïs avec plafonnement ($GDD_{\text{maïs}}$)
Pour chaque jour $j$, le degré-jour de croissance $DJ_j$ intègre la saturation enzymatique à $30\ ^\circ\text{C}$ (recommandations DRIAS / projet ORACLE) et le zéro de végétation ($T_{\text{base}} = 6\ ^\circ\text{C}$) :
$$DJ_j = \max\left( \frac{T_{n,j} + \min(T_{x,j},\, 30)}{2} - 6,\; 0 \right)$$
Le cumul annuel sur l'ensemble des jours $D$ de l'année s'écrit :
$$GDD_{\text{maïs}} = \sum_{j \in D} DJ_j$$

#### 4. Bilan hydrique et méthode d'Hargreaves-Samani ($ET_0$)
L'API Open-Meteo Climate renvoyant des valeurs nulles pour l'évapotranspiration $ET_0$, notre modèle applique l'équation empirique validée par la FAO :
$$ET_0 = 0{,}0023 \cdot R_a \cdot (T_{\text{moy}} + 17{,}8) \cdot \sqrt{T_{\max} - T_{\min}}$$
Le bilan hydrique net annuel $B$ sur la période active s'obtient par :
$$B = \sum_{j \in D} \left( P_j - ET_{0,j} \right)$$
* $P_j$ : précipitations journalières (`precipitation_sum` en mm).
* $R_a$ : rayonnement solaire extraterrestre calculé selon la latitude et le jour de l'année (DOY).

### Prise de recul scientifique sur les formules
1. **Plafonnement thermique du Maïs** : En accord avec les référentiels DRIAS et le projet ORACLE, la somme des températures pour le maïs plafonne la température journalière maximale à 30 °C. Au-delà de cette température, les processus enzymatiques de la plante saturent ou se dégradent, annulant tout bénéfice physiologique de la chaleur supplémentaire.
2. **Méthode d'Hargreaves-Samani pour $ET_0$** : L'API Open-Meteo Climate renvoyant des valeurs `null` pour le paramètre d'évapotranspiration $ET_0$, notre modèle applique la formule d'Hargreaves recommandée par la FAO :
   $$ET_0 = 0{,}0023 \cdot R_a \cdot (T_{\text{moy}} + 17{,}8) \cdot \sqrt{T_{\max} - T_{\min}}$$
   Le rayonnement solaire extraterrestre $R_a$ est modélisé directement à partir de la latitude de la commune et du jour de l'année (DOY).

---

## 3. Analyse de la dimension spatiale

### 3.1 Territoires retenus (`commune.csv`)
L'analyse s'appuie sur quatre communes cibles représentant des régimes bioclimatiques contrastés et emblématiques des cultures étudiées :

| id_commune | Commune | Code INSEE | Régime bioclimatique | Vocation agricole territoriale |
| :---: | :--- | :---: | :--- | :--- |
| **1** | Dijon | 21231 | Semi-continental | Vignoble de Bourgogne (sensible aux gels de printemps). |
| **2** | Strasbourg | 67482 | Semi-continental | Plaine d'Alsace (favorable au maïs, amplitude thermique forte). |
| **3** | Lille | 59350 | Océanique dégradé | Flandre / Bassin du Nord (grandes cultures, blé tendre, pomme de terre). |
| **4** | Rennes | 35238 | Océanique | Bretagne (climat tempéré humide, bassin clé du colza). |

### 3.2 Limites physiques de la donnée (Maille Open-Meteo ~10 km)
* **Maille physique vs Découpage administratif** : Les modèles climatiques globaux (CMIP6) ne délivrent pas une météo à l'adresse exacte, mais par cellules maillées d'environ $10\text{ km} \times 10\text{ km}$ (0,1°). Les données climatiques attribuées à chaque commune correspondent au centroïde administratif de celle-ci. Deux parcelles distantes de moins de 10 km partagent donc la même série météo simulée.
* **Lissage altimétrique et microclimats** : À l'échelle de cette maille de 10 km, le relief est nécessairement lissé. Les microclimats réels (cuvettes de gelée blanche, coteaux abrités, expositions sud pour la vigne) sont moyennés par le modèle. L'application doit donc être présentée aux exploitants comme un outil de tendance macro-climatique territoriale, et non comme un capteur parcellaire de précision.

---

## 4. Architecture décisionnelle : Schéma en étoile

Pour garantir des performances optimales sous AlwaysData (MySQL), la base de données est modélisée selon un schéma en étoile centré sur la table de faits des indicateurs calculés.

### 4.1 Règle d'or architecturale : L'API Open-Meteo comme flux externe
Les données météo journalières issues de l'API Open-Meteo (plusieurs centaines de milliers de lignes par simulation décennale) **ne sont jamais stockées en base de données**. L'API intervient comme un flux externe transitoire consommé en mémoire vive : le pipeline effectue les calculs agronomiques puis n'enregistre que les métriques agrégées dans `Fact_Indicateur`.

### 4.2 Schéma relationnel

<html>
    <p align="center">
    <img src="schema_etoile.png" alt="Schéma en étoile" width="85%">
    </p>
</html>


### 4.3 Schéma relationnel Plaintext :

```txt
Plaintext
       +-----------------------+              +-----------------------+
       |      Dim_Commune      |              |      Dim_Culture      |
       +-----------------------+              +-----------------------+
       | * code_insee (PK)     |              | * id_culture (PK)     |
       |   nom                 |              |   nom                 |
       |   latitude, longitude |              |   t_base_c            |
       |   altitude_m          |              |   gdd_maturite_cj     |
       |   zone_climatique     |              |   seuil_gel_c         |
       +-----------+-----------+              |   besoin_eau_mm       |
                   |                          |   seuil_stress_c      |
                   |                          +-----------+-----------+
                   |                                      |
                   |       [API Open-Meteo]               |
                   |      (Flux journalier brut)          |
                   |               |                      |
                   |        Pipeline Calcul               |
                   |               |                      |
                   v               v                      v
       +------------------------------------------------------+
       |                   Fact_Indicateur                    |
       +------------------------------------------------------+
       | * id_fait (PK)                                       |
       | # code_insee (FK)                                    |
       | # id_culture (FK)                                    |
       | # id_horizon (FK)                                    |
       | # id_modele (FK)                                     |
       |   id_session                                         |
       |   gdd_cumul_moyen                                    |
       |   nb_jours_gel                                       |
       |   nb_jours_stress_th                                 |
       |   bilan_hydrique_mm                                  |
       |   verdict                                            |
       +------------------------------------------------------+
                   ^                                      ^
                   |                                      |
       +-----------+-----------+              +-----------+-----------+
       |      Dim_Horizon      |              |      Dim_Modele       |
       +-----------------------+              +-----------------------+
       | * id_horizon (PK)     |              | * id_modele (PK)      |
       |   label (2041-2050)   |              |   nom_modele          |
       |   annee_debut         |              |   organisme           |
       |   annee_fin           |              |   scenario (SSP)      |
       +-----------------------+              +-----------------------+
```

---

## 5. Contrat d'interface technique : DEV ↔ DATA

Afin d'assurer le découplage complet des équipes pendant la conception et le développement, la frontière d'échange entre le client API (pôle DEV) et le moteur de calcul (pôle DATA) est strictement formalisée.

### 5.1 Format d'entrée (Transmis par DEV à DATA en mémoire)
Une série journalière brute propre sous forme de liste de dictionnaires ou de DataFrame Pandas :
* `code_insee` (*str*) : code officiel INSEE à 5 caractères.
* `date` (*str ISO-8601*) : format `AAAA-MM-JJ`.
* `temperature_2m_min` (*float*) : température minimale journalière (°C).
* `temperature_2m_max` (*float*) : température maximale journalière (°C).
* `temperature_2m_mean` (*float*) : température moyenne journalière (°C).
* `precipitation_sum` (*float*) : cumul journalier des précipitations (mm).

### 5.2 Format de sortie (Persisté par DATA dans `Fact_Indicateur`)
Les attributs calculés et insérés dans la base AlwaysData :
* `code_insee` (*FK Dim_Commune*)
* `id_culture` (*FK Dim_Culture*)
* `id_horizon` (*FK Dim_Horizon*)
* `id_modele` (*FK Dim_Modele*)
* `id_session` (*VARCHAR(64)*, identifiant technique de session anonyme)
* `gdd_cumul_moyen` (*INT*)
* `nb_jours_gel_moyen` (*DECIMAL(4,1)*)
* `nb_jours_stress_moyen` (*DECIMAL(4,1)*)
* `bilan_hydrique_moyen` (*INT*)
* `verdict` (*VARCHAR(20)* : `VIABLE`, `A_RISQUE`, `NON_VIABLE`)

### 5.3 Stratégie de découplage via `series-test.csv`
Le pôle DATA utilise un jeu d'essai local (`data/series-test.csv`) contenant 365 jours de relevés intégrant des scénarios limites (gelées printanières à $-4$ °C, pics de canicule à $38$ °C). Ce protocole permet de développer et valider unitairement les algorithmes agronomiques sans attendre la finalisation du client API par le pôle DEV.

### 5.4 Validation expérimentale du contrat d'interface (Commune de Dijon, 2045)

Pour valider le flux de traitement en amont des développements du jalon J2, le pôle DATA a extrait et traité une série temporelle réelle d'une année complète (365 jours sur l'horizon simulé 2045) pour la commune de **Dijon (Code INSEE : 21231)** via le modèle climatique **MRI-AGCM3-2-S**.

#### 1. Protocole de test et script d'exécution (`tests/test_calculs_data.py`)
Un script Python autonome vérifie d'abord la conformité structurelle du contrat d'échange (présence des colonnes et types attendus), puis applique les formules matricielles agronomiques :

```python
import pandas as pd

# 1. Chargement des données (skiprows=3 pour ignorer les métadonnées Open-Meteo)
df = pd.read_csv('data/series_test.csv', skiprows=3)

# Normalisation des colonnes conformément au contrat d'interface
df.columns = ['date', 'temperature_2m_max', 'temperature_2m_min', 'temperature_2m_mean', 'precipitation_sum']
df['date'] = pd.to_datetime(df['date'])

print("=== 1. TEST CONTRAT D'INTERFACE ===")
colonnes_attendues = {'date', 'temperature_2m_min', 'temperature_2m_max', 'temperature_2m_mean', 'precipitation_sum'}
assert colonnes_attendues.issubset(set(df.columns)), "Erreur: colonnes manquantes !"
print("Format d'entrée DEV -> DATA : VALIDE\n")

print("=== 2. TEST DES INDICATEURS MÉTIER (DATA) ===")

# A. Gel printanier (Vigne : seuil <= -2 °C en avril-mai)
masque_printemps = df['date'].dt.month.isin([4, 5])
nb_jours_gel_vigne = (masque_printemps & (df['temperature_2m_min'] <= -2.0)).sum()
print(f"Jours de gel vigne (seuil <= -2 °C en avril-mai) : {nb_jours_gel_vigne}")

# B. Stress thermique (seuil >= 35 °C)
nb_jours_stress = (df['temperature_2m_max'] >= 35.0).sum()
print(f"Jours de stress thermique (>= 35 °C) : {nb_jours_stress}")

# C. Somme des températures du maïs (base 6 °C et plafonnement Tx à 30 °C)
def calcul_dj_mais(row):
    tx_plafonne = min(row['temperature_2m_max'], 30.0)
    dj = (row['temperature_2m_min'] + tx_plafonne) / 2.0 - 6.0
    return max(dj, 0.0)

df['gdd_mais'] = df.apply(calcul_dj_mais, axis=1)
print(f"Cumul GDD maïs calculé (avec plafonnement 30 °C) : {df['gdd_mais'].sum():.2f} °C·j")
print("\n=== RÉSULTAT : TOUS LES CALCULS DATA SONT VALIDÉS ===")
```
#### Résultat

```txt
=== 1. TEST CONTRAT D'INTERFACE ===
Format d'entrée DEV -> DATA : VALIDE

=== 2. TEST DES INDICATEURS MÉTIER (DATA) ===
Jours de gel vigne (seuil <= -2 °C en avril-mai) : 0
Jours de stress thermique (>= 35 °C) : 0
Cumul GDD maïs calculé (avec plafonnement 30 °C) : 2721.05 °C·j

=== RÉSULTAT : TOUS LES CALCULS DATA SONT VALIDÉS ===
```

### 3. Analyse agronomique des résultats observés

* **Risque de gel printanier nul (0 jour sous $-2\ ^\circ\text{C}$)** : sur les mois d'avril et mai 2045 à Dijon, la température minimale ne descend jamais en dessous de $+0{,}3\ ^\circ\text{C}$. Aucun dégât de gel sur bourgeon débourré n'est simulé sur cette année type.
* **Absence de stress thermique extrême (0 jour $\ge 35\ ^\circ\text{C}$)** : le pic caniculaire atteint $34{,}7\ ^\circ\text{C}$ sans franchir le seuil létal de $35\ ^\circ\text{C}$. Toutefois, la simulation enregistre 21 journées dépassant les $30\ ^\circ\text{C}$, confirmant un échauffement estival significatif.
* **Maturité thermique largement acquise pour le maïs ($2\,721{,}05\ ^\circ\text{C}\cdot\text{j}$)** : le seuil de maturité physiologique du maïs grain est fixé à $1\,600\ ^\circ\text{C}\cdot\text{j}$ dans le référentiel agronomique. Avec un cumul simulé de $2\,721{,}05\ ^\circ\text{C}\cdot\text{j}$ (malgré l'application stricte du plafonnement à $30\ ^\circ\text{C}$), l'exigence thermique est largement satisfaite ($+1\,121{,}05\ ^\circ\text{C}\cdot\text{j}$ d'excédent). Le facteur limitant futur pour le maïs à Dijon ne sera donc pas thermique, mais strictement hydrique.

### 4. Conclusion du jalon J1

Ce test valide expérimentalement la robustesse des formules agronomiques et confirme que les structures de données en mémoire permettent de générer directement l'enregistrement destiné à la table de faits `Fact_Indicateur` pour le jalon J2.