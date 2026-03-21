import os

INFINI = float("inf")


def charger_graphe(numero_graphe, dossier="graphs"):
    """
    Charge un graphe depuis un fichier texte nommé 'graph{numero}.txt'
    dans le dossier spécifié.

    Format du fichier attendu :
        Ligne 1 : nombre de sommets
        Ligne 2 : nombre d'arcs
        Lignes suivantes : sommet_origine  sommet_destination  valeur

    Retourne la matrice d'adjacence du graphe (liste de listes).
    Retourne None si le fichier est introuvable ou mal formaté.
    """
    nom_fichier = os.path.join(dossier, f"graph{numero_graphe}.txt")

    # Vérification de l'existence du fichier
    if not os.path.exists(nom_fichier):
        print(f"  Erreur : le fichier '{nom_fichier}' est introuvable.")
        return None

    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            lignes = fichier.read().splitlines()

        # Lecture du nombre de sommets et d'arcs
        nb_sommets = int(lignes[0].strip())
        nb_arcs = int(lignes[1].strip())

        # Initialisation de la matrice : infini partout, 0 sur la diagonale
        matrice = [[INFINI] * nb_sommets for _ in range(nb_sommets)]
        for i in range(nb_sommets):
            matrice[i][i] = 0

        # Lecture de chaque arc
        for idx in range(2, 2 + nb_arcs):
            parties = lignes[idx].strip().split()
            origine = int(parties[0])
            destination = int(parties[1])
            valeur = int(parties[2])
            matrice[origine][destination] = valeur

        print(f"  Graphe n°{numero_graphe} chargé avec succès "
              f"({nb_sommets} sommets, {nb_arcs} arcs).")
        return matrice

    except (ValueError, IndexError) as erreur:
        print(f"  Erreur lors de la lecture du fichier '{nom_fichier}' : {erreur}")
        return None