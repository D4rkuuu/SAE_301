from copy import copy
from datetime import date
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


ROOT = Path(r"c:\Document\BUT3 - Semestre 1\SAE 301")
SOURCE = ROOT / "Classeur1.xlsx"
DESTINATION = ROOT / "Classeur1_corrige.xlsx"

header_fill = PatternFill("solid", fgColor="1F4E78")
header_font = Font(color="FFFFFF", bold=True)
warning_fill = PatternFill("solid", fgColor="FFF2CC")


def style_sheet(sheet):
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions
    for cell in sheet[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)
    for index, column_cells in enumerate(sheet.columns, start=1):
        length = max(len(str(cell.value or "")) for cell in column_cells)
        sheet.column_dimensions[get_column_letter(index)].width = min(max(length + 2, 12), 42)
    sheet.row_dimensions[1].height = 34


def write_table(sheet, headers, rows):
    sheet.append(headers)
    for row in rows:
        sheet.append(row)
    style_sheet(sheet)


try:
    workbook = load_workbook(SOURCE)
except FileNotFoundError:
    workbook = Workbook()

for sheet_name in list(workbook.sheetnames):
    del workbook[sheet_name]

cultures = [
    ["Maïs grain", "Zea mays L.", "annuelle", 6, 1340, 1655, None, None, None, 35, "GDD maïs France; Tx plafonnée à 30 °C", "partiellement vérifiée"],
    ["Tournesol", "Helianthus annuus L.", "annuelle", None, None, None, None, None, None, None, "À sourcer par variété et stade", "non sourcée"],
    ["Soja", "Glycine max (L.) Merr.", "annuelle", 10, None, None, None, None, None, None, "GDD dépendant du groupe de maturité", "partiellement vérifiée"],
    ["Vigne (raisin de cuve)", "Vitis vinifera L.", "pérenne", 10, 1300, 1300, -2, None, 25, 35, "Gel à -2 °C au débourrement; seuil dépendant du stade", "partiellement vérifiée"],
    ["Olivier", "Olea europaea L.", "pérenne", None, None, None, None, None, 25, None, "Pas de GDD universel; utiliser Kc et phénologie", "non sourcée"],
]

dim_culture = workbook.create_sheet("Dim_Culture")
write_table(
    dim_culture,
    ["culture", "nom_scientifique", "type", "t_base_gdd_c", "gdd_maturite_min_cj", "gdd_maturite_max_cj", "seuil_gel_c", "besoin_eau_mm", "t_opt_min_c", "seuil_stress_thermique_c", "remarque", "confiance"],
    cultures,
)
for row in dim_culture.iter_rows(min_row=2):
    if row[-1].value != "vérifiée":
        for cell in row:
            cell.fill = warning_fill

sources = [
    ["Maïs grain", "t_base_gdd_c", 6, 6, 6, "ARVALIS / amorçage DATA", "https://www.arvalis.fr", date(2026, 9, 14), "partiellement vérifiée", "Convention française base 6 °C; à confirmer avec une fiche ARVALIS précise."],
    ["Maïs grain", "gdd_maturite_cj", 1600, 1340, 1655, "ARVALIS / amorçage DATA", "https://www.arvalis.fr", date(2026, 9, 14), "partiellement vérifiée", "Fourchette dépendante de la précocité variétale."],
    ["Tournesol", "t_base_gdd_c", None, None, None, "FAO 56; source technique à compléter", "https://www.fao.org/4/X0490E/X0490E00.htm", date(2026, 9, 14), "non sourcée", "Ne pas reprendre la valeur du classeur sans fiche variétale vérifiée."],
    ["Soja", "t_base_gdd_c", 10, None, None, "Purdue University", "https://www.extension.purdue.edu/extmedia/ay/ay-217-w.pdf", date(2026, 9, 14), "source unique", "Le groupe de maturité et la formule GDD doivent être précisés."],
    ["Vigne (raisin de cuve)", "t_base_gdd_c", 10, 10, 10, "UC Agriculture and Natural Resources", "https://my.ucanr.edu/sites/viticulture-fresno/files/286798.pdf", date(2026, 9, 14), "source unique", "Convention de somme thermique viticole."],
    ["Vigne (raisin de cuve)", "gdd_maturite_cj", 1300, None, None, "Amorçage DATA; à recouper IFV", "https://www.vignevin.com", date(2026, 9, 14), "source unique", "Valeur indicative pour le raisin de cuve, dépendante du cépage."],
    ["Vigne (raisin de cuve)", "seuil_gel_c", -2, None, None, "IFV / Ephytia INRAE", "https://ephytia.inrae.fr", date(2026, 9, 14), "source unique", "Valable au débourrement; le bourgeon dormant supporte des températures différentes."],
    ["Olivier", "Kc_et_bilan_hydrique", None, None, None, "FAO 56", "https://www.fao.org/4/X0490E/X0490E00.htm", date(2026, 9, 14), "vérifiée pour la méthode", "La FAO documente Kc et le bilan hydrique, pas un seuil GDD universel."],
]

source_sheet = workbook.create_sheet("Source_Seuil")
write_table(
    source_sheet,
    ["culture", "nom_seuil", "valeur", "valeur_min", "valeur_max", "source", "url", "date_consultee", "confiance", "justification"],
    sources,
)

indicators = [
    ["GDD / maturité", "temperature_2m_min + temperature_2m_max", "Σ max(0, ((Tn + min(Tx, 30)) / 2) - t_base)", "Fenêtre de culture définie par Dim_Temps", "atteint si cumul >= gdd_maturite"],
    ["Jours de gel critiques", "temperature_2m_min", "nombre de jours où Tn <= seuil_gel", "Débourrement / floraison selon la culture", "risque si le nombre dépasse le seuil choisi"],
    ["Stress thermique", "temperature_2m_max", "nombre de jours où Tx > seuil_stress", "Saison ou stade sensible", "seuil et durée à documenter"],
    ["Bilan hydrique", "precipitation_sum + ET0", "Σ(pluie - ET0)", "Saison de culture", "comparer au besoin ou au Kc par stade"],
    ["Viabilité", "résultats des indicateurs", "combinaison GDD + gel + stress + eau", "Horizon et modèle", "viable / à risque / non viable"],
]

indicator_sheet = workbook.create_sheet("Indicateurs")
write_table(indicator_sheet, ["indicateur", "variables_api", "formule", "fenetre", "sortie"], indicators)

rules_sheet = workbook.create_sheet("Regles_Qualite")
write_table(
    rules_sheet,
    ["règle", "décision"],
    [
        ["Séries climatiques", "Ne pas stocker les séries brutes; elles servent au calcul."],
        ["Faits", "Stocker les indicateurs calculés dans Fact_Indicateur."],
        ["Sources", "Chaque seuil possède sa propre source, URL, date et confiance."],
        ["Valeurs manquantes", "Utiliser n.d.; ne jamais mettre 0 par défaut."],
        ["Incertitude", "Conserver les bornes min/max lorsque les sources divergent."],
        ["Modèles", "Comparer au moins deux modèles climatiques; ce ne sont pas des scénarios."],
        ["ET0", "La calculer par Hargreaves si la variable Open-Meteo est nulle."],
        ["Maillage", "Calculer à l'échelle du centroïde de la commune; résolution API environ 10 km."],
    ],
)

for sheet in workbook.worksheets:
    sheet.sheet_view.showGridLines = False

workbook.save(DESTINATION)
print(DESTINATION)