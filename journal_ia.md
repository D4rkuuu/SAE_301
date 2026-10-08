## [11/09/2026] — Initialisation du format du journal (DEV)

**Exemple de tableau remplis pour le journal :**

| Date    | Équipier | Outil/modèle | Tâche / contexte   | Prompt (résumé)                                 | Sortie IA        | Gardé/modifié/rejeté | Justification (vérif. / correction / test)                                                | Tokens (≈) |
|---------|----------|--------------|--------------------|-------------------------------------------------|------------------|----------------------|-------------------------------------------------------------------------------------------|------------|
| 12/10   | Léa      | Haiku 4.5    | requête SQL des GDD | « somme des T° > 10 °C par culture et commune » | requête proposée | **modifié**          | jointure fausse sur `Dim_Temps` corrigée ; index ajouté ; testée sur commune X → cohérent | ~1 900     |
| remplir | les      | infos        | ici                | ...                                             | ...              | ...                  | ...                                                                                       | ...        |

*(Ajoutez autant de lignes que nécessaire.)*

# **JOURNAL IA**

| Date | Équipier   | Outil/modèle | Tâche / contexte | Prompt (résumé) | Sortie IA | Gardé/modifié/rejeté | Justification (vérif. / correction / test) | Tokens (≈) |
|---|------------|---|---|---|---|---|---|---|
| 08/10 | Adrien Roj | Gemini | Rédaction du contrat d'interface `contrat_interface.md` | « Crée-moi un exemple de contrat d'interface entre DEV et DATA » | Exemple de contrat avec structure JSON d'échange | **modifié** | Ajout des métadonnées de commune (`code_insee`, `nom_commune`) et de culture (`culture_id`) oubliées initialement par l'IA, indispensables pour que DATA croise avec la BDD. Ajout de commentaires explicatifs pour clarifier les attentes. | non mesurable |
|  |  |  |  |  |  |  |  |  |