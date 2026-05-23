Description
Ce projet implémente l'algorithme de Floyd-Warshall permettant de calculer les chemins de valeurs minimales entre tous les couples de sommets d'un graphe orienté et valué. Il a été réalisé dans le cadre du cours SM601 - Théorie des graphes, année 2025/2026.



Structure du projet
Le dossier racine contient les trois fichiers Python du programme (main.py, floyd_warshall.py, chargeur_graphe.py), le fichier de traces d'exécution (execution_trace.txt), ainsi que le rapport PDF. Les fichiers de graphes sont regroupés dans un sous-dossier graphs/ qui contient les 14 fichiers texte graph1.txt à graph14.txt.
Lancement du programme
Prérequis : Python 3 installé sur la machine.
Se placer dans le dossier racine du projet (là où se trouve main.py), puis lancer :
python main.py
Le programme demande ensuite le numéro du graphe à analyser. Il est possible de tester plusieurs graphes successivement sans relancer le programme. Pour quitter, taper quitter ou q.

Description des fichiers
main.py
Point d'entrée du programme. Gère la boucle principale, la saisie utilisateur, l'affichage des résultats et la reconstruction des chemins.
floyd_warshall.py
Contient l'algorithme de Floyd-Warshall, la détection de circuit absorbant, la reconstruction des chemins via la matrice des prédécesseurs, et les fonctions d'affichage des matrices L et P.
chargeur_graphe.py
Lit le fichier texte du graphe, construit la matrice d'adjacence en mémoire et ne retouche plus jamais le fichier ensuite.
execution_trace.txt
Traces d'exécution du programme sur l'ensemble des graphes de test (graph1 à graph13) ainsi que sur le graphe applicatif (graph14).
Recherche_des_billets_avion_moins_chers_Europe_Floyd_Warshall.pdf
Rapport décrivant l'exemple réel modélisé (réseau aérien européen), les données, les résultats et leur interprétation.

Format des fichiers graphes
Chaque fichier graph{n}.txt suit le format suivant : la première ligne indique le nombre de sommets, la deuxième le nombre d'arcs, puis chaque ligne suivante décrit un arc sous la forme sommet_origine  sommet_destination  valeur.
Exemple avec 4 sommets et 5 arcs :

4
5
0 1 1
0 2 5
1 2 3
1 3 5
2 3 2

Fonctionnalités

Chargement d'un graphe depuis un fichier texte
Affichage de la matrice d'adjacence initiale avec les numéros de sommets en en-tête
Exécution de Floyd-Warshall avec affichage des matrices L et P à chaque étape intermédiaire
Détection automatique des circuits absorbants
Affichage interactif des chemins les plus courts entre deux sommets au choix

Fonctionnalités

Chargement d'un graphe depuis un fichier texte
Affichage de la matrice d'adjacence initiale
Exécution de Floyd-Warshall avec affichage des matrices L et P à chaque étape
Détection automatique des circuits absorbants
Affichage interactif des chemins les plus courts entre deux sommets
