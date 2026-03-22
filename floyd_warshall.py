INFINI = float("inf")


# float("inf") représente l'infini en Python
# on l'utilise pour dire "pas de chemin direct" entre deux sommets


def floyd_warshall(matrice):
    n = len(matrice)
    # len() retourne le nombre de lignes = nombre de sommets du graphe

    # Copie de la matrice d'adjacence pour ne pas modifier l'original
    # [ligne[:] for ligne in matrice] copie chaque ligne indépendamment
    # sans le [:], toutes les lignes pointeraient vers le même objet en mémoire
    L = [ligne[:] for ligne in matrice]

    # Initialisation de la matrice des prédécesseurs
    # [[None] * n for _ in range(n)] crée une matrice n x n remplie de None
    # le _ signifie qu'on n'a pas besoin du numéro d'itération
    # None = on ne connaît pas encore le prédécesseur
    P = [[None] * n for _ in range(n)]

    # Pour chaque arc existant, le prédécesseur direct de j depuis i est i lui-même
    for i in range(n):
        for j in range(n):
            if i != j and matrice[i][j] != INFINI:
                P[i][j] = i

    print("\n=== Matrices initiales (avant itérations) ===")
    afficher_matrice(L, "L initiale")
    afficher_matrice_pred(P, "P initiale")

    # Triple boucle principale de Floyd-Warshall
    # k = sommet intermédiaire qu'on autorise à chaque étape
    # i = sommet de départ, j = sommet d'arrivée
    for k in range(n):
        for i in range(n):
            for j in range(n):

                # On vérifie que les deux chemins i->k et k->j existent
                # sans cette vérification on risque d'additionner inf + inf
                if L[i][k] != INFINI and L[k][j] != INFINI:

                    # Coeur de l'algorithme : est-ce que passer par k est plus court ?
                    if L[i][k] + L[k][j] < L[i][j]:
                        L[i][j] = L[i][k] + L[k][j]

                        # On met à jour le prédécesseur de j en venant de i
                        # P[k][j] contient le dernier sommet avant j sur le chemin k->j
                        P[i][j] = P[k][j]

        print(f"\n=== Étape k = {k} ===")
        afficher_matrice(L, f"L (k={k})")
        afficher_matrice_pred(P, f"P (k={k})")

    return L, P


def contient_circuit_absorbant(L):
    # Un circuit absorbant = cycle dont la somme des valeurs est négative
    # Floyd-Warshall le détecte en regardant la diagonale de L
    # Si L[i][i] < 0, il existe un chemin qui part de i, fait un tour et revient
    # à i avec un coût négatif = circuit absorbant
    n = len(L)
    for i in range(n):
        if L[i][i] < 0:
            return True
    return False


def obtenir_chemin(P, depart, arrivee):
    # Si P[depart][arrivee] est None, aucun chemin n'existe
    if P[depart][arrivee] is None:
        return []

    chemin = []
    courant = arrivee

    # On remonte les prédécesseurs depuis l'arrivée jusqu'au départ
    # à chaque tour on ajoute le sommet courant puis on recule d'un cran
    while courant != depart:
        chemin.append(courant)
        precedent = P[depart][courant]

        # Protection contre une boucle infinie si P est incohérente
        if precedent is None:
            return []
        courant = precedent

    # On ajoute le sommet de départ car la boucle s'arrête avant de l'inclure
    chemin.append(depart)

    # reverse() inverse la liste sur place car on a construit le chemin à l'envers
    # ex: [4, 9, 0] devient [0, 9, 4]
    chemin.reverse()
    return chemin


def afficher_matrice(L, titre="Matrice"):
    n = len(L)
    largeur = 7

    print(f"\n  {titre} :")

    # On construit l'en-tête des colonnes avec les numéros de sommets
    # f"{j:>{largeur}}" aligne le nombre j à droite sur 'largeur' caractères
    entete = "     " + "".join(f"{j:>{largeur}}" for j in range(n))
    print(entete)
    print("     " + "-" * (largeur * n))

    for i in range(n):
        ligne = f"{i:>3} |"
        for j in range(n):
            if L[i][j] == float("inf"):
                # On affiche "inf" à la place de 1e+308 pour plus de lisibilité
                ligne += f"{'inf':>{largeur}}"
            else:
                ligne += f"{L[i][j]:>{largeur}}"
        print(ligne)


def afficher_matrice_pred(P, titre="Prédécesseurs"):
    n = len(P)
    largeur = 7

    print(f"\n  {titre} :")

    entete = "     " + "".join(f"{j:>{largeur}}" for j in range(n))
    print(entete)
    print("     " + "-" * (largeur * n))

    for i in range(n):
        ligne = f"{i:>3} |"
        for j in range(n):
            valeur = P[i][j]
            # On affiche "_" à la place de None pour indiquer l'absence de prédécesseur
            if valeur is None:
                ligne += f"{'_':>{largeur}}"
            else:
                ligne += f"{valeur:>{largeur}}"
        print(ligne)