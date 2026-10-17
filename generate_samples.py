import json
import os
from controllers.api_client import fetch_weather_data, format_to_dev_contract

def main():
    print("Récupération des données climatiques d'exemple depuis Open-Meteo...")

    # Paramètres imposés par le contrat d'interface
    modele = "MRI_AGCM3_2_S"
    horizon = "2041-2050"

    # Récupération sur une année future entière (2050) à Toulouse
    raw_data = fetch_weather_data(
        lat=43.60,
        lon=1.44,
        start_date="2050-01-01",
        end_date="2050-12-31",
        modele=modele
    )

    formatted_data = format_to_dev_contract(
        raw_data=raw_data,
        code_insee="31555",
        nom_commune="Toulouse",
        culture_id="ble_tendre",
        horizon=horizon,
        modele=modele
    )

    # Création du dossier data/ s'il n'existe pas pour éviter une erreur
    os.makedirs("data", exist_ok=True)

    # Sauvegarde directe dans le dossier data/
    output_path = "data/series-exemple.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)

    print(f"Fichier généré avec succès dans '{output_path}' !")

if __name__ == "__main__":
    main()