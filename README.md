Solveur de Sudoku
📌 Contexte
Ce projet est un solveur de Sudoku développé en Python avec Pygame pour l'interface graphique. L'objectif est de résoudre automatiquement des grilles de Sudoku en utilisant différentes approches algorithmiques, allant des méthodes naïves à des techniques plus optimisées basées sur des heuristiques.

🧠 Algorithmes utilisés
1. Brute Force
Une première approche a été d'explorer la résolution par force brute, c'est-à-dire en testant toutes les combinaisons possibles jusqu'à trouver une solution valide. Cette méthode, bien que fonctionnelle, est extrêmement inefficace car elle ne prend en compte aucune stratégie d'optimisation.

2. Backtracking (Retour sur trace)
Le backtracking est une technique plus efficace qui fonctionne en essayant d'assigner des valeurs aux cases tout en respectant les règles du Sudoku. Si une contradiction est détectée, l'algorithme revient en arrière pour essayer une autre option. Cette approche réduit considérablement le nombre de tentatives nécessaires par rapport au brute force.

3. Backtracking amélioré avec heuristiques
Pour optimiser encore plus le backtracking, nous avons intégré des heuristiques :

Heuristique du choix minimum : toujours essayer d'insérer un chiffre dans la case ayant le moins d'options possibles.

Propagation des contraintes : mise à jour des possibilités après chaque attribution de valeur.

Ordre de parcours optimisé : privilégier les cases les plus contraignantes en premier.

Cette version améliorée du backtracking s'est avérée être la meilleure solution en termes de rapidité et d'efficacité.

🛠️ Outils utilisés
Python : Langage principal du projet.

Pygame : Utilisé pour l'affichage et l'interaction avec l'utilisateur.

Fichiers .txt : Chargement des grilles de Sudoku depuis des fichiers prédéfinis.

🔍 Veille technologique
Durant le développement, une veille a été réalisée sur les méthodes de résolution de Sudoku, notamment :

Comparaison des performances entre brute force, backtracking et heuristiques.

Étude des solveurs avancés utilisant la logique et l’intelligence artificielle.

✅ Conclusion
Le backtracking classique offre déjà une amélioration significative par rapport au brute force, mais son efficacité peut être fortement améliorée grâce aux heuristiques. Ces optimisations permettent une résolution bien plus rapide des grilles, même pour les plus complexes.

Ce projet a permis d'explorer et d'expérimenter différentes stratégies algorithmiques pour un problème combinatoire classique, avec une application interactive via Pygame.
