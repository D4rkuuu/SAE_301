import uuid
import requests


def fetch_weather_data(lat: float, lon: float, start_date: str, end_date: str) -> dict:
    """Récupère les données climatiques pour les deux modèles du contrat v1.8 en un seul appel."""
    url = "https://climate-api.open-meteo.com/v1/climate"

    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "models": "MRI_AGCM3_2_S,EC_Earth3P_HR",
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "precipitation_sum",
            "et0_fao_evapotranspiration_sum",
        ],
        "timezone": "Europe/Paris",
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_to_dev_contract(
    raw_data: dict,
    code_insee: str,
    nom_commune: str,
    id_culture: int,
    id_horizon: int,
    horizon: str,
    id_session: str | None = None,
) -> list[dict]:
    """Découpe la réponse Open-Meteo en un objet par modèle selon le contrat v1.8."""
    daily = raw_data.get("daily", {})
    dates = daily.get("time", [])
    session_id = id_session or str(uuid.uuid4())
    modeles = ["MRI_AGCM3_2_S", "EC_Earth3P_HR"]

    resultats = []
    for nom_modele in modeles:
        tmins = daily.get(f"temperature_2m_min_{nom_modele}", daily.get("temperature_2m_min", []))
        tmaxs = daily.get(f"temperature_2m_max_{nom_modele}", daily.get("temperature_2m_max", []))
        tmoys = daily.get(f"temperature_2m_mean_{nom_modele}", daily.get("temperature_2m_mean", []))
        precips = daily.get(f"precipitation_sum_{nom_modele}", daily.get("precipitation_sum", []))
        et0s = daily.get(
            f"et0_fao_evapotranspiration_sum_{nom_modele}",
            daily.get("et0_fao_evapotranspiration_sum", []),
        )

        series_meteo = []
        for date, tmin, tmax, tmoy, precip, et0 in zip(dates, tmins, tmaxs, tmoys, precips, et0s):
            series_meteo.append(
                {
                    "date": date,
                    "t_min": tmin,
                    "t_max": tmax,
                    "t_moy": tmoy,
                    "precip": precip if precip is not None else 0.0,
                    "et0": et0 if et0 is not None else 0.0,
                }
            )

        resultats.append(
            {
                "metadonnees": {
                    "code_insee": code_insee,
                    "nom_commune": nom_commune,
                    "latitude": raw_data.get("latitude"),
                    "longitude": raw_data.get("longitude"),
                    "id_culture": id_culture,
                    "id_horizon": id_horizon,
                    "horizon": horizon,
                    "nom_modele": nom_modele,
                    "id_session": session_id,
                },
                "series_meteo": series_meteo,
            }
        )

    return resultats