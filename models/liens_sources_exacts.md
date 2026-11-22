# Liens exacts des sources

Les liens ci-dessous indiquent l'endroit qui contient effectivement l'information. Un lien vers l'accueil d'un organisme n'est pas utilisé comme preuve.

## Coefficients d'eau Kc

- [FAO-56, chapitre 6, tableaux Kc](https://www.fao.org/4/x0490e/x0490e0b.htm#tabulated-kc-values) : tableaux 11 et 12, avec les coefficients Kc par stade. On y trouve notamment le maïs grain, le tournesol, le soja, la vigne et l'olivier.
- [FAO-56, calcul de l'ETc](https://www.fao.org/4/x0490e/x0490e0b.htm#calculating-etc) : formule `ETc = Kc x ETo` et construction de la courbe Kc.
- [FAO-56, olivier](https://www.fao.org/4/x0490e/x0490e0b.htm#crop-coefficients) : la ligne `Olives (40 to 60% ground coverage by canopy)` donne `Kc initial = 0.65`, `Kc mi-saison = 0.70`, `Kc fin = 0.70`.
- [FAO-56, vigne de cuve](https://www.fao.org/4/x0490e/x0490e0b.htm#crop-coefficients) : la ligne `Grapes - Wine` donne `Kc initial = 0.30`, `Kc mi-saison = 0.70`, `Kc fin = 0.45`.
- [FAO-56, tournesol](https://www.fao.org/4/x0490e/x0490e0b.htm#crop-coefficients) : la ligne `Sunflower` donne `Kc initial = 0.35`, `Kc mi-saison = 1.15`, `Kc fin = 0.35`.
- [FAO-56, soja](https://www.fao.org/4/x0490e/x0490e0b.htm#crop-coefficients) : la ligne `Soybeans` donne `Kc mi-saison = 1.15` et `Kc fin = 0.50`; la valeur initiale n'est pas donnée comme une valeur spécifique au soja dans cette table.
- [FAO-56, maïs grain](https://www.fao.org/4/x0490e/x0490e0b.htm#crop-coefficients) : la ligne `Maize, Field (grain)` donne `Kc mi-saison = 1.20` et `Kc fin = 0.60-0.35`.

## Evapotranspiration

- [FAO-56, Hargreaves](https://www.fao.org/4/x0490e/x0490e07.htm#an-alternative-equation-for-eto-when-weather-data-are-missing) : équation 52, `ETo = 0.0023 (Tmean + 17.8) (Tmax - Tmin)^0.5 Ra`.
- [FAO-56, Penman-Monteith](https://www.fao.org/4/x0490e/x0490e06.htm#fao-penman-monteith-equation) : méthode de référence si les données météo nécessaires sont disponibles.

## Températures et sommes thermiques

- [Purdue University, soja](https://www.extension.purdue.edu/extmedia/ay/ay-217-w.pdf) : PDF direct sur la croissance et le développement du soja. Le PDF doit être téléchargé pour consulter la page exacte, car son contenu n'est pas exposé par le serveur web.
- [UC Agriculture and Natural Resources, vigne](https://my.ucanr.edu/sites/viticulture-fresno/files/286798.pdf) : PDF direct sur les unités thermiques de la vigne.
- [Ephytia-INRAE, gel de la vigne](https://ephytia.inrae.fr/fr/C/6050/Vigne-Gel) : page directe INRAE sur les dégâts et périodes de nuisibilité liés au gel de la vigne.
- [ECOCROP FAO, recherche des exigences culturales](https://ecocrop.apps.fao.org/ecocrop/srv/en/cropSearchForm) : formulaire officiel de recherche. Il ne fournit pas une URL stable par culture sans identifiant de fiche ; aucune température n'est donc présentée comme sourcée par une simple URL générique.

## Valeurs à ne pas présenter comme vérifiées

Les valeurs `t_min_c`, `t_opt_min_c`, `t_opt_max_c`, `t_max_c`, `seuil_stress_thermique_c` et plusieurs GDD ne sont pas universelles : elles dépendent de la variété et du stade. Tant qu'une fiche précise d'ARVALIS, Terres Inovia, IFV ou France Olive n'est pas attachée à la valeur, le CSV conserve `n.d.` au lieu d'un chiffre inventé.