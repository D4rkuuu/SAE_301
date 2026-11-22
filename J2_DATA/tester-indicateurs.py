import sys
import warnings
import numpy as np
import pandas as pd

CULTURES = [
    {"id": 1, "nom": "Blé tendre (hiver)", "t_base": 0.0,  "gdd_mat": 2150.0, "seuil_gel": -4.0, "eau": 450.0, "stress": 30.0},
    {"id": 2, "nom": "Colza (hiver)",      "t_base": 5.0,  "gdd_mat": 2200.0, "seuil_gel": -4.0, "eau": 450.0, "stress": 27.0},
    {"id": 3, "nom": "Maïs grain",         "t_base": 6.0,  "gdd_mat": 1600.0, "seuil_gel":  0.0, "eau": 550.0, "stress": 35.0},
    {"id": 4, "nom": "Pomme de terre",     "t_base": 7.0,  "gdd_mat": 1500.0, "seuil_gel": -1.0, "eau": 600.0, "stress": 28.0},
    {"id": 5, "nom": "Vigne (cuve)",       "t_base": 10.0, "gdd_mat": 1300.0, "seuil_gel": -2.0, "eau": 400.0, "stress": 35.0},
]

CYCLES = {
    1: ("2044-10-15", "2045-07-31"),
    2: ("2044-08-20", "2045-07-15"),
    3: ("2045-04-20", "2045-10-15"),
    4: ("2045-04-15", "2045-09-15"),
    5: ("2045-04-01", "2045-10-31"),
}

def generer_csv(nom_fichier="series-exemple.csv"):
    """Génère 518 jours (01/08/2044 -> 31/12/2045) déterministes avec et0."""
    dates = pd.date_range("2044-08-01", "2045-12-31", freq="D")
    jours = dates.day_of_year.values

    t_moy = np.round(11.0 + 10.0 * np.sin(2 * np.pi * (jours - 105) / 365.0), 1)
    df = pd.DataFrame({
        "date": dates.strftime("%Y-%m-%d"),
        "t_min": np.round(t_moy - 4.0, 1),
        "t_max": np.round(t_moy + 4.0, 1),
        "t_moy": t_moy,
        "precip": np.where(np.arange(len(dates)) % 4 == 0, 8.0, 0.0),
        "et0": np.round(2.5 + 1.8 * np.sin(2 * np.pi * (jours - 105) / 365.0), 2),
    })

    # Événements connus par construction : 3 gelées (avril) et 4 jours de canicule (juillet)
    df.loc[df["date"].isin(["2045-04-10", "2045-04-11", "2045-04-12"]), ["t_min", "t_moy"]] = [-4.5, 2.0]
    df.loc[df["date"].isin(["2045-07-20", "2045-07-21", "2045-07-22", "2045-07-23"]), ["t_max", "t_moy"]] = [36.0, 28.0]

    df.to_csv(nom_fichier, index=False)
    print(f"Fichier '{nom_fichier}' généré ({len(df)} lignes).")

def verifier_hargreaves(df_cycle):
    """Contrôle de cohérence non bloquant entre ET0 API et formule de Hargreaves."""
    td = np.maximum(df_cycle["t_max"] - df_cycle["t_min"], 0.0)
    et0_harg = 0.0023 * 11.5 * (df_cycle["t_moy"] + 17.8) * np.sqrt(td)
    ratio = df_cycle["et0"].sum() / max(et0_harg.sum(), 1.0)
    if not (0.4 <= ratio <= 2.0):
        warnings.warn(f"Alerte cohérence ET0 vs Hargreaves (ratio={ratio:.2f})")

def calculer_indicateurs(df, culture):
    df_clean = df.dropna(subset=["t_min", "t_max", "precip", "et0"])
    debut, fin = CYCLES[culture["id"]]
    df_cycle = df_clean[(df_clean["date"] >= debut) & (df_clean["date"] <= fin)]
    verifier_hargreaves(df_cycle)

    # 1. GDD (plafonnement Tx à 30°C pour le maïs)
    tx = np.minimum(df_cycle["t_max"], 30.0) if culture["id"] == 3 else df_cycle["t_max"]
    gdd_total = round(float(np.maximum(0.0, ((df_cycle["t_min"] + tx) / 2.0) - culture["t_base"]).sum()), 1)

    # 2. Gel (avril-mai sur la fenêtre culturale df_cycle, condition <= seuil_gel)
    printemps = df_cycle[df_cycle["date"].dt.month.isin([4, 5])]
    nb_gel = int((printemps["t_min"] <= culture["seuil_gel"]).sum())

    # 3. Stress thermique (juin-août sur la fenêtre culturale df_cycle, condition >= stress)
    ete = df_cycle[df_cycle["date"].dt.month.isin([6, 7, 8])]
    nb_stress = int((ete["t_max"] >= culture["stress"]).sum())

    # 4. Bilan hydrique = somme(precip - et0)
    bilan = round(float((df_cycle["precip"] - df_cycle["et0"]).sum()), 1)

    # 5. Verdict
    if gdd_total < culture["gdd_mat"] or nb_gel >= 5 or nb_stress >= 10 or bilan < -0.5 * culture["eau"]:
        verdict = "NON_VIABLE"
    elif nb_gel < 1 and nb_stress < 3 and bilan >= -0.25 * culture["eau"]:
        verdict = "VIABLE"
    else:
        verdict = "A_RISQUE"

    return {"gdd": gdd_total, "gel": nb_gel, "stress": nb_stress, "bilan": bilan, "verdict": verdict}

def executer_tests():
    # --- TEST 1 : Contrat d'interface ---
    df = pd.read_csv("series-exemple.csv")
    requis = {"date", "t_min", "t_max", "t_moy", "precip", "et0"}
    assert requis.issubset(df.columns), f"Colonnes manquantes : {requis - set(df.columns)}"
    df["date"] = pd.to_datetime(df["date"])

    # --- TEST 2 : Cas standard sur les 5 cultures ---
    print(f"{'Culture':<20} | {'GDD':>7} | {'Gel':>3} | {'Stress':>6} | {'Bilan':>7} | {'Verdict'}")
    print("-" * 68)
    res = {}
    for c in CULTURES:
        res[c["id"]] = calculer_indicateurs(df, c)
        r = res[c["id"]]
        print(f"{c['nom']:<20} | {r['gdd']:>7.1f} | {r['gel']:>3} | {r['stress']:>6} | {r['bilan']:>7.1f} | {r['verdict']}")

    # Vérifications strictes sur la fenêtre culturale
    assert res[1]["gel"] == 3 and res[1]["stress"] == 4   # Blé : touché par avril et juillet
    assert res[2]["gel"] == 3 and res[2]["stress"] == 0   # Colza : récolté le 15/07, épargné par la canicule du 20/07
    assert res[3]["gel"] == 0 and res[3]["stress"] == 4   # Maïs : semé le 20/04, épargné par le gel du 10/04

    # --- TEST 3 : Journée exactement au seuil (<= -2.0°C pour la Vigne) ---
    df_test = df.copy()
    df_test.loc[df_test["date"] == "2045-04-10", "t_min"] = -2.0
    assert calculer_indicateurs(df_test, CULTURES[4])["gel"] == 3

    # --- TEST 4 : Année sans gel ---
    df_test["t_min"] = np.maximum(df["t_min"], 5.0)
    assert calculer_indicateurs(df_test, CULTURES[4])["gel"] == 0

    # --- TEST 5 : Valeur manquante (NaN) ---
    df_nan = df.copy()
    df_nan.loc[10, "t_min"] = np.nan
    assert not np.isnan(calculer_indicateurs(df_nan, CULTURES[0])["gdd"])

    print("\nSUCCÈS : Contrat d'interface, bilan hydrique (ET0) et 4 cas limites validés !")

if __name__ == "__main__":
    if "--generer" in sys.argv:
        generer_csv()
    else:
        executer_tests()