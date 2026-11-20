import requests

url = "https://climate-api.open-meteo.com/v1/climate"

params = {
    "latitude": 47.32,   # Dijon
    "longitude": 5.04,
    "start_date": "2040-01-01",
    "end_date": "2041-12-31",
    "models": "MRI_AGCM3_2_S,EC_Earth3P_HR",
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,et0_fao_evapotranspiration_sum",
    "timezone": "Europe/Paris"
}

print("Appel de l'API..")
try:
    response = requests.get(url, params=params, timeout=15)

    if response.status_code == 200:
        data = response.json()
        daily = data["daily"]
        dates = daily["time"]

        print(f"5 premières dates récupérées ({len(dates)} jours au total) :")
        print(dates[:5])

        for cle, valeurs in daily.items():
            if cle == "time":
                continue
            manquantes = [d for d, v in zip(dates, valeurs) if v is None]
            if manquantes:
                print(f"- {cle} : {len(manquantes)} manquantes ({manquantes[0]} -> {manquantes[-1]})")
            else:
                print(f"- {cle} : 0 manquante | 5 premières valeurs : {valeurs[:5]}")
    else:
        print(f"Erreur HTTP : {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"La connexion à l'API a échoué : {e}")