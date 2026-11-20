import requests


def fetch_weather_data(
        lat: float, lon: float, start_date: str, end_date: str, modele: str = "MRI_AGCM3_2_S"
) -> dict:
    """Récupère les données climatiques projetées depuis l'API Open-Meteo Climate."""
    url = "https://climate-api.open-meteo.com/v1/climate"

    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "models": modele,
        "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum"],
        "timezone": "Europe/Paris",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_to_dev_contract(
        raw_data: dict, code_insee: str, nom_commune: str, culture_id: str, horizon: str, modele: str
) -> dict:
    """Transforme les données brutes d'Open-Meteo au format du contrat DEV -> DATA."""
    daily = raw_data.get("daily", {})
    dates = daily.get("time", [])
    tmins = daily.get("temperature_2m_min", [])
    tmaxs = daily.get("temperature_2m_max", [])
    tmoys = daily.get("temperature_2m_mean", [])
    precips = daily.get("precipitation_sum", [])

    series_meteo = []
    for date, tmin, tmax, tmoy, precip in zip(dates, tmins, tmaxs, tmoys, precips):
        series_meteo.append(
            {
                "date": date,
                "t_min": tmin,
                "t_max": tmax,
                "t_moy": tmoy,
                "precip": precip if precip is not None else 0.0,
            }
        )

    return {
        "metadonnees": {
            "code_insee": code_insee,
            "nom_commune": nom_commune,
            "latitude": raw_data.get("latitude"),
            "longitude": raw_data.get("longitude"),
            "culture_id": culture_id,
            "horizon": horizon,
            "modele": modele,
        },
        "series_meteo": series_meteo,
    }