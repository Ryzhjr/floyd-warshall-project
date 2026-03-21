

from chargeur_graphe import charger_graphe
from floyd_warshall import (
    floyd_warshall,
    contient_circuit_absorbant,
    obtenir_chemin,
    afficher_matrice,
)

INFINI = float("inf")


def afficher_separateur():
    print("\n" + "=" * 60)


def boucle_chemins(L, P):
    """
    Boucle interactive permettant à l'utilisateur de demander
    le chemin le plus court entre deux sommets.
    """
    n = len(L)

    while True:
        print("\nVoulez-vous afficher un chemin ? (oui / non)")
        reponse = input("  > ").strip().lower()

        if reponse not in ("oui", "o"):
            print("  Fin de l'affichage des chemins.")
            break

        try:
            depart = int(input(f"  Sommet de départ (0 à {n - 1}) : ").strip())
            arrivee = int(input(f"  Sommet d'arrivée (0 à {n - 1}) : ").strip())
        except ValueError:
            print("  Erreur : veuillez entrer des numéros de sommets valides.")
            continue

        # Vérification des bornes
        if not (0 <= depart < n and 0 <= arrivee < n):
            print(f"  Erreur : les sommets doivent être compris entre 0 et {n - 1}.")
            continue

        if depart == arrivee:
            print(f"  Le sommet de départ et d'arrivée sont identiques ({depart}).")
            continue

        distance = L[depart][arrivee]

        if distance == INFINI:
            print(f"  Aucun chemin n'existe entre le sommet {depart} et le sommet {arrivee}.")
            continue

        chemin = obtenir_chemin(P, depart, arrivee)

        if not chemin:
            print(f"  Aucun chemin n'existe entre le sommet {depart} et le sommet {arrivee}.")
        else:
            chemin_str = " → ".join(str(s) for s in chemin)
            print(f"\n  Chemin le plus court : {chemin_str}")
            print(f"  Valeur totale        : {distance}")


def traiter_graphe(numero_graphe):
    """
    Charge et traite un graphe complet :
    lecture, affichage, Floyd-Warshall, détection de circuit absorbant,
    puis affichage des chemins si pas de circuit absorbant.
    """
    afficher_separateur()
    print(f"  Traitement du graphe n°{numero_graphe}")
    afficher_separateur()

    # Étape 1 : Chargement du graphe
    matrice = charger_graphe(numero_graphe)
    if matrice is None:
        return

    # Étape 2 : Affichage de la matrice d'adjacence initiale
    print("\n=== Matrice d'adjacence initiale ===")
    afficher_matrice(matrice, "Matrice initiale")

    # Étape 3 : Exécution de Floyd-Warshall
    print("\n\n=== Exécution de l'algorithme de Floyd-Warshall ===")
    L, P = floyd_warshall(matrice)

    # Étape 4 : Affichage des matrices finales
    afficher_separateur()
    print("=== Matrices finales ===")
    afficher_matrice(L, "L finale (distances minimales)")

    # Étape 5 : Détection d'un circuit absorbant
    afficher_separateur()
    if contient_circuit_absorbant(L):
        print("  ⚠ Le graphe contient au moins un CIRCUIT ABSORBANT.")
        print("  Les chemins les plus courts ne peuvent pas être calculés.")
        return

    print("  ✓ Aucun circuit absorbant détecté.")

    # Étape 6 : Affichage interactif des chemins
    afficher_separateur()
    print("=== Recherche de chemins les plus courts ===")
    boucle_chemins(L, P)


def main():
    """
    Boucle principale du programme.
    Permet de traiter plusieurs graphes successivement sans relancer le programme.
    """
    print("=" * 60)
    print("   Algorithme de Floyd-Warshall — Chemins les plus courts")
    print("=" * 60)

    while True:
        print("\nEntrez le numéro du graphe à analyser (ou 'quitter' pour terminer) :")
        saisie = input("  > ").strip().lower()

        if saisie in ("quitter", "q"):
            print("\n  Au revoir !")
            break

        try:
            numero = int(saisie)
        except ValueError:
            print("  Erreur : veuillez entrer un numéro de graphe valide.")
            continue

        traiter_graphe(numero)


if __name__ == "__main__":
    main()

