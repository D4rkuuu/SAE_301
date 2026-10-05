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