import os

# os permet de travailler avec les fichiers et dossiers du système
# on l'utilise pour vérifier si un fichier existe et construire son chemin

INFINI = float("inf")


# float("inf") représente l'infini en Python
# on l'utilise pour les cases de la matrice où il n'y a pas d'arc


def charger_graphe(numero_graphe, dossier="graphs"):
    # On construit le chemin vers le fichier
    # os.path.join est plus fiable que d'écrire "graphs/graph1.txt" à la main
    # car il s'adapte automatiquement à Windows (\) et Linux/Mac (/)
    nom_fichier = os.path.join(dossier, f"graph{numero_graphe}.txt")

    # On vérifie que le fichier existe avant d'essayer de l'ouvrir
    # évite une erreur FileNotFoundError si l'utilisateur entre un mauvais numéro
    if not os.path.exists(nom_fichier):
        print(f"  Erreur : le fichier '{nom_fichier}' est introuvable.")
        return None

    try:
        # "r" = mode lecture seule
        # encoding="utf-8" évite les problèmes avec les accents
        # with garantit que le fichier sera bien fermé après la lecture
        # même si une erreur survient pendant la lecture
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            # read() lit tout le contenu d'un coup
            # splitlines() découpe en liste de lignes sans les \n
            # ex: "4\n5\n3 1 25" -> ["4", "5", "3 1 25"]
            lignes = fichier.read().splitlines()

        # Les deux premières lignes contiennent le nombre de sommets et d'arcs
        # strip() enlève les espaces invisibles éventuels en début/fin de ligne
        # int() convertit la chaîne en entier
        nb_sommets = int(lignes[0].strip())
        nb_arcs = int(lignes[1].strip())

        # On initialise la matrice avec infini partout
        # [INFINI] * nb_sommets crée une ligne remplie d'infini
        # on en crée nb_sommets pour avoir une matrice carrée n x n
        matrice = [[INFINI] * nb_sommets for _ in range(nb_sommets)]

        # La diagonale vaut 0 : le coût pour rester sur place est nul
        for i in range(nb_sommets):
            matrice[i][i] = 0

        # On lit chaque arc à partir de la ligne 3 (indice 2)
        # range(2, 2 + nb_arcs) génère les indices 2, 3, 4... jusqu'au dernier arc
        for idx in range(2, 2 + nb_arcs):
            # split() découpe la ligne aux espaces et retourne une liste de chaînes
            # ex: "3 1 25" -> ["3", "1", "25"]
            parties = lignes[idx].strip().split()
            origine = int(parties[0])
            destination = int(parties[1])
            valeur = int(parties[2])

            # On place la valeur de l'arc dans la case correspondante
            matrice[origine][destination] = valeur

        print(f"  Graphe n°{numero_graphe} chargé avec succès "
              f"({nb_sommets} sommets, {nb_arcs} arcs).")
        return matrice

    except (ValueError, IndexError) as erreur:
        # ValueError : levée si int() reçoit autre chose qu'un nombre
        # ex: int("abc") -> ValueError
        # IndexError : levée si on essaie d'accéder à une ligne qui n'existe pas
        # ex: lignes[5] alors que le fichier n'a que 3 lignes -> IndexError
        # on attrape les deux pour afficher un message clair sans planter
        print(f"  Erreur lors de la lecture du fichier '{nom_fichier}' : {erreur}")
        return None