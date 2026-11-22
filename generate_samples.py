import json
import os
from controllers.api_client import fetch_weather_data, format_to_dev_contract


def main():
    print("Récupération des données climatiques d'exemple depuis Open-Meteo...")

    raw_data = fetch_weather_data(
        lat=43.60,
        lon=1.44,
        start_date="2039-08-01",
        end_date="2049-12-31",
    )

    formatted_data = format_to_dev_contract(
        raw_data=raw_data,
        code_insee="31555",
        nom_commune="Toulouse",
        id_culture=1,
        id_horizon=3,
        horizon="2040-2049",
    )

    os.makedirs("data", exist_ok=True)
    output_path = "data/series-exemple.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)

    print(f"Fichier généré avec succès dans '{output_path}' !")


if __name__ == "__main__":
    main() 