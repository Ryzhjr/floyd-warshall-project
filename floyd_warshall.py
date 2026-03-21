import math

INFINI = float("inf")


def floyd_warshall(matrice):
    """
    Exécute l'algorithme de Floyd-Warshall sur la matrice d'adjacence donnée.
    Retourne la matrice des distances (L) et la matrice des prédécesseurs (P).
    Affiche L et P à chaque étape intermédiaire.
    """
    n = len(matrice)

    # Initialisation de la matrice des distances L (copie de la matrice d'adjacence)
    L = [ligne[:] for ligne in matrice]

    # Initialisation de la matrice des prédécesseurs P
    P = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and matrice[i][j] != INFINI:
                P[i][j] = i  # le prédécesseur de j en venant de i est i lui-même

    print("\n=== Matrices initiales (avant itérations) ===")
    afficher_matrice(L, "L initiale")
    afficher_matrice_pred(P, "P initiale")

    # Triple boucle principale de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if L[i][k] != INFINI and L[k][j] != INFINI:
                    if L[i][k] + L[k][j] < L[i][j]:
                        L[i][j] = L[i][k] + L[k][j]
                        P[i][j] = P[k][j]

        print(f"\n=== Étape k = {k} ===")
        afficher_matrice(L, f"L (k={k})")
        afficher_matrice_pred(P, f"P (k={k})")

    return L, P


def contient_circuit_absorbant(L):
    """
    Vérifie si le graphe contient un circuit absorbant.
    Un circuit absorbant est détecté si L[i][i] < 0 pour un sommet i.
    """
    n = len(L)
    for i in range(n):
        if L[i][i] < 0:
            return True
    return False


def obtenir_chemin(P, depart, arrivee):
    """
    Reconstruit le chemin le plus court entre 'depart' et 'arrivee'
    à partir de la matrice des prédécesseurs P.
    Retourne une liste de sommets, ou une liste vide si aucun chemin n'existe.
    """
    if P[depart][arrivee] is None:
        return []  # Aucun chemin entre ces deux sommets

    chemin = []
    courant = arrivee

    # On remonte les prédécesseurs de arrivee jusqu'à depart
    while courant != depart:
        chemin.append(courant)
        precedent = P[depart][courant]
        if precedent is None:
            return []  # Protection contre boucle infinie
        courant = precedent

    chemin.append(depart)
    chemin.reverse()
    return chemin


def afficher_matrice(L, titre="Matrice"):
    """
    Affiche une matrice de distances de façon lisible,
    avec les numéros de sommets en en-tête.
    """
    n = len(L)
    largeur = 7  # largeur de chaque cellule

    print(f"\n  {titre} :")

    # En-tête des colonnes
    entete = "     " + "".join(f"{j:>{largeur}}" for j in range(n))
    print(entete)
    print("     " + "-" * (largeur * n))

    # Lignes
    for i in range(n):
        ligne = f"{i:>3} |"
        for j in range(n):
            if L[i][j] == float("inf"):
                ligne += f"{'inf':>{largeur}}"
            else:
                ligne += f"{L[i][j]:>{largeur}}"
        print(ligne)


def afficher_matrice_pred(P, titre="Prédécesseurs"):
    """
    Affiche la matrice des prédécesseurs de façon lisible.
    """
    n = len(P)
    largeur = 7

    print(f"\n  {titre} :")

    # En-tête des colonnes
    entete = "     " + "".join(f"{j:>{largeur}}" for j in range(n))
    print(entete)
    print("     " + "-" * (largeur * n))

    # Lignes
    for i in range(n):
        ligne = f"{i:>3} |"
        for j in range(n):
            valeur = P[i][j]
            if valeur is None:
                ligne += f"{'_':>{largeur}}"
            else:
                ligne += f"{valeur:>{largeur}}"
        print(ligne)