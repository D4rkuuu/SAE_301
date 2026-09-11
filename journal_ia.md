## [11/09/2026] — Initialisation du format du journal (DEV)

* **Outil utilisé** : Gemini
* **Prompt / Question posée** : "À quoi doit ressembler le journal_ia.md d'après les docs ?"
* **Résultat fourni par l'IA** : Explication des règles de traçabilité imposées par le sujet (pas d'IA en source BDD, obligation de vérifier les données/code) et proposition d'un modèle Markdown avec les champs : Outil, Prompt, Résultat, Vérification, Décision.
* **Vérification effectuée** : Relecture des documents d'amorçage (`14-amorcage-DATA-referentiel-seuils.pdf`, section §7.2) pour valider que le modèle répond bien aux exigences du sujet.
* **Décision & Intégration** : Modèle retenu et appliqué immédiatement pour créer le fichier `JOURNAL_IA.md` à la racine du dépôt Git.