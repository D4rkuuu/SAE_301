import requests

API_URL = "https://climate-api.open-meteo.com/v1/climate"

MODELES = [
    "MRI_AGCM3_2_S",
    "EC_Earth3P_HR",
]

VARIABLES = {
    "temperature_2m_max": "T° max (°C)",
    "temperature_2m_min": "T° min (°C)",
    "precipitation_sum": "Précipitations (mm)",
    "et0_fao_evapotranspiration_sum": "ET0 FAO (mm)",
}


def recuperer_donnees(latitude, longitude, debut, fin):
    """Appelle Open-Meteo et renvoie le bloc 'daily' (ou None en cas d'erreur)."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": debut,
        "end_date": fin,
        "models": ",".join(MODELES),
        "daily": ",".join(VARIABLES.keys()),
    }

    try:
        response = requests.get(API_URL, params=params, timeout=15)
        response.raise_for_status()
        return response.json()["daily"]
    except requests.exceptions.HTTPError:
        print(f"Erreur HTTP {response.status_code} : {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Échec de connexion à l'API : {e}")
    return None


def afficher_rapport(daily, ville):
    """Affiche un résumé aligné par modèle climatique."""
    dates = daily["time"]
    print(f"\n=== {ville} | {dates[0]} -> {dates[-1]} ({len(dates)} jours) ===")

    for modele in MODELES:
        print(f"\nModèle : {modele}")
        print("-" * 72)

        for var_api, label in VARIABLES.items():
            cle = f"{var_api}_{modele}"
            valeurs = daily[cle]
            manquantes = [d for d, v in zip(dates, valeurs) if v is None]

            if manquantes:
                statut = f"{len(manquantes)} manquantes"
                detail = f"({manquantes[0]} -> {manquantes[-1]})"
            else:
                statut = "OK (0 manquante)"
                detail = f"ex: {valeurs[:3]}"

            print(f"  {label:<22} | {statut:<18} | {detail}")


if __name__ == "__main__":
    print("Appel de l'API Open-Meteo...")
    daily = recuperer_donnees(
        latitude=47.32,
        longitude=5.04,
        debut="2040-01-01",
        fin="2041-12-31",
    )
    if daily:
        afficher_rapport(daily, ville="Dijon")