import requests

url = "https://climate-api.open-meteo.com/v1/climate"

params = {
    "latitude": 43.60,
    "longitude": 1.44,
    "start_date": "2049-01-01",
    "end_date": "2049-12-31",
    "models": "MRI_AGCM3_2_S",
    "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum"],
    "timezone": "Europe/Paris"
}

print("Appel de l'API..")
try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print("5 premières dates récupérées :")
        print(data['daily']['time'][:5])
        print("Températures max correspondantes :")
        print(data['daily']['temperature_2m_max'][:5])
        print("Températures moyennes correspondantes :")
        print(data['daily']['temperature_2m_mean'][:5])
    else:
        print(f"Erreur HTTP : {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"La connexion à l'API a échoué : {e}")