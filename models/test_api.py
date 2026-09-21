import requests

url = "https://climate-api.open-meteo.com/v1/climate"

params = {
    "latitude": 43.60,
    "longitude": 1.44,
    "start_date": "2049-01-01",
    "end_date": "2049-12-31",
    "models": "MRI_AGCM3_2_S",
    "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
    "timezone": "Europe/Paris"
}

print("Appel de l'API en cours...")
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Succès ! Voici les 5 premières dates récupérées :")
    print(data['daily']['time'][:5])
    print("Températures max correspondantes :")
    print(data['daily']['temperature_2m_max'][:5])
else:
    print(f"Erreur HTTP : {response.status_code}")