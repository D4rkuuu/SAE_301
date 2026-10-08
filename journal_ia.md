## [11/09/2026] — Initialisation du format du journal (DEV)

**Exemple de tableau remplis pour le journal :**

| Date    | Équipier | Outil/modèle | Tâche / contexte   | Prompt (résumé)                                 | Sortie IA        | Gardé/modifié/rejeté | Justification (vérif. / correction / test)                                                | Tokens (≈) |
|---------|----------|--------------|--------------------|-------------------------------------------------|------------------|----------------------|-------------------------------------------------------------------------------------------|------------|
| 12/10   | Léa      | Haiku 4.5    | requête SQL des GDD | « somme des T° > 10 °C par culture et commune » | requête proposée | **modifié**          | jointure fausse sur `Dim_Temps` corrigée ; index ajouté ; testée sur commune X → cohérent | ~1 900     |
| remplir | les      | infos        | ici                | ...                                             | ...              | ...                  | ...                                                                                       | ...        |

*(Ajoutez autant de lignes que nécessaire.)*

# **JOURNAL IA**

| Date  | Équipier   | Outil/modèle | Tâche / contexte | Prompt (résumé)                                                                                                                                              | Sortie IA | Gardé/modifié/rejeté | Justification (vérif. / correction / test) | Tokens (≈)    |
|-------|------------|--------------|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---------------|
| 08/10 | Adrien Roj | Gemini       | Rédaction du contrat d'interface `contrat_interface.md` | « Crée-moi un exemple de contrat d'interface entre DEV et DATA »                                                                                             | Exemple de contrat avec structure JSON d'échange | **modifié** | Ajout des métadonnées de commune (`code_insee`, `nom_commune`) et de culture (`culture_id`) oubliées initialement par l'IA, indispensables pour que DATA croise avec la BDD. Ajout de commentaires explicatifs pour clarifier les attentes. | non mesurable |
| 08/10 | Adrien Roj | Gemini       | Implémentation du module API météo et du script d'export d'échantillon | « Créer moi et explique moi pas à pas le fonctionnement du code de api_client et crée-moi un fichier generate_samples qui suit la logique de notre contrat » | Code des deux scripts Python (controllers/api_client.py et generate_samples.py) avec explications pas à pas | gardé | Code testé et exécuté avec succès. Séparation validée entre la logique de production (api_client.py) et le script de test manuel (generate_samples.py). L'échantillon JSON généré sert d'exemple de référence pour l'équipe DATA. Ce travail prépare l'intégration dynamique dans Flask, où l'application utilisera directement api_client.py selon les choix de l'utilisateur (ex. Vigne de 2025 à 2026). | non mesurable |