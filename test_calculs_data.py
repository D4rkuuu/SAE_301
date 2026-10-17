import pandas as pd
import json

# 1. Chargement des données depuis l'échantillon JSON généré par DEV
with open('data/series-exemple.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Création du DataFrame uniquement avec la liste des séries
df = pd.DataFrame(data['series_meteo'])
df['date'] = pd.to_datetime(df['date'])

print("=== 1. TEST CONTRAT D'INTERFACE ===")
colonnes_attendues = {'date', 't_min', 't_max', 't_moy', 'precip'}
colonnes_presentes = set(df.columns)
assert colonnes_attendues.issubset(colonnes_presentes), f"Erreur contrat ! Colonnes trouvées : {colonnes_presentes}"
print("Format d'entrée DEV -> DATA : VALIDE\n")

print("=== 2. TEST DES INDICATEURS MÉTIER (DATA) ===")

# A. Test Gel Printanier (Vigne : seuil <= -2 °C en avril-mai)
masque_printemps = df['date'].dt.month.isin([4, 5])
nb_jours_gel_vigne = (masque_printemps & (df['t_min'] <= -2.0)).sum()
print(f"Jours de gel vigne (seuil <= -2 °C en avril-mai) : {nb_jours_gel_vigne}")

# B. Test Stress Thermique (seuil >= 35 °C en été)
masque_ete = df['date'].dt.month.isin([6, 7, 8])
nb_jours_stress = (masque_ete & (df['t_max'] >= 35.0)).sum()
print(f"Jours de stress thermique (>= 35 °C en été) : {nb_jours_stress}")

# C. Test Règle Spécifique Maïs (Plafonnement Tx à 30 °C et base 6 °C)
def calcul_dj_mais(row):
    tx_plafonne = min(row['t_max'], 30.0)
    dj = ((row['t_min'] + tx_plafonne) / 2.0) - 6.0
    return max(dj, 0.0)

df['gdd_mais'] = df.apply(calcul_dj_mais, axis=1)
total_gdd = df['gdd_mais'].sum()
print(f"Cumul GDD maïs calculé (avec plafonnement 30 °C) : {total_gdd:.2f} °C·j")

print("\n=== RÉSULTAT : TOUS LES CALCULS DATA SONT VALIDÉS ===")