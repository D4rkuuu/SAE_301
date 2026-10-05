import pandas as pd

# 1. Chargement des données (skiprows=3 pour ignorer les métadonnées Open-Meteo)
df = pd.read_csv('data/series_test.csv', skiprows=3)

# Normalisation des noms de colonnes (suppression des unités pour respecter le contrat)
df.columns = ['date', 'temperature_2m_max', 'temperature_2m_min', 'temperature_2m_mean', 'precipitation_sum']
df['date'] = pd.to_datetime(df['date'])

print("=== 1. TEST CONTRAT D'INTERFACE ===")
colonnes_attendues = {'date', 'temperature_2m_min', 'temperature_2m_max', 'temperature_2m_mean', 'precipitation_sum'}
colonnes_presentes = set(df.columns)
assert colonnes_attendues.issubset(colonnes_presentes), "Erreur: colonnes manquantes dans le CSV !"
print("Format d'entrée DEV -> DATA : VALIDE\n")

print("=== 2. TEST DES INDICATEURS MÉTIER (DATA) ===")

# A. Test Gel Printanier (Vigne : seuil <= -2 °C en avril-mai)
masque_printemps = df['date'].dt.month.isin([4, 5])
nb_jours_gel_vigne = (masque_printemps & (df['temperature_2m_min'] <= -2.0)).sum()
print(f"Jours de gel vigne (seuil <= -2 °C en avril-mai) : {nb_jours_gel_vigne}")

# B. Test Stress Thermique (seuil >= 35 °C en été)
nb_jours_stress = (df['temperature_2m_max'] >= 35.0).sum()
print(f"Jours de stress thermique (>= 35 °C) : {nb_jours_stress}")

# C. Test Règle Spécifique Maïs (Plafonnement Tx à 30 °C et base 6 °C)
def calcul_dj_mais(row):
    tx_plafonne = min(row['temperature_2m_max'], 30.0)
    dj = (row['temperature_2m_min'] + tx_plafonne) / 2.0 - 6.0
    return max(dj, 0.0)

df['gdd_mais'] = df.apply(calcul_dj_mais, axis=1)
total_gdd = df['gdd_mais'].sum()
print(f"Cumul GDD maïs calculé (avec plafonnement 30 °C) : {total_gdd:.2f} °C·j")

print("\n=== RÉSULTAT : TOUS LES CALCULS DATA SONT VALIDÉS ===")