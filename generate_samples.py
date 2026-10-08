import json
from controllers.api_client import fetch_weather_data, format_to_dev_contract


def main():
    print("Récupération des données météo d'exemple depuis Open-Meteo...")

    # Exemple pour Toulouse sur les 3 premiers jours de 2024
    raw_data = fetch_weather_data(
        lat=43.6, lon=1.44, start_date="2024-01-01", end_date="2024-01-10"
    )

    formatted_data = format_to_dev_contract(
        raw_data=raw_data,
        code_insee="31555",
        nom_commune="Toulouse",
        culture_id="ble_tendre",
        annee=2024,
    )

    # Sauvegarde directe dans le dossier data/
    output_path = "data/series-exemple.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)

    print(f"Fichier généré avec succès dans '{output_path}' !")


if __name__ == "__main__":
    main()