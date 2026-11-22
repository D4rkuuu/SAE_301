# Sources du référentiel cultures

Ce fichier accompagne `referentiel_cultures.csv`. Les valeurs du classeur Excel initial n'ont pas été reprises.

## Sources vérifiées

- [FAO 56 - Crop evapotranspiration](https://www.fao.org/4/X0490E/X0490E00.htm) : méthode de référence pour l'évapotranspiration, les coefficients culturaux et le bilan hydrique. Le document contient aussi les cultures annuelles, la vigne et un exemple de couvert d'olivier.
- [FAO 56 - Chapter 9](https://www.fao.org/3/x0490e/x0490e0f.htm) : limites d'utilisation des coefficients et exemple de calcul pour l'olivier. Cette source ne donne pas un seuil universel de gel ou de chaleur pour l'olivier.
- [Iowa State University - Growing degree days](https://www.extension.iastate.edu/agdm/crops/a1-80.html) : référence universitaire pour les sommes de températures du maïs.
- [FAO 56 - Crop evapotranspiration](https://www.fao.org/4/X0490E/X0490E00.htm) : source vérifiée utilisée pour le tournesol dans l'attente d'une fiche variétale qui fixe sa base thermique et ses stades.
- [Purdue University - Soybean growth and development](https://www.extension.purdue.edu/extmedia/ay/ay-217-w.pdf) : référence universitaire pour le développement et les sommes thermiques du soja.
- [University of California Cooperative Extension - Grapevine heat units](https://my.ucanr.edu/sites/viticulture-fresno/files/286798.pdf) : référence universitaire pour les unités thermiques de la vigne.

## Règles de qualité

- Une valeur dépendante de la variété ou du stade ne doit pas être transformée en seuil universel.
- `n.d.` signifie « non documenté dans les sources retenues », et non zéro.
- Les seuils de gel devront être ajoutés après choix d'un stade précis : semis, levée, débourrement, floraison ou maturation.
- Les seuils de stress thermique devront préciser la durée : température maximale journalière, nombre de jours consécutifs ou température horaire.
- Avant insertion en base, chaque valeur ajoutée doit conserver son URL, sa date de consultation et son unité.