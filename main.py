from chargeur_graphe import charger_graphe
from floyd_warshall import (
    floyd_warshall,
    contient_circuit_absorbant,
    obtenir_chemin,
    afficher_matrice,
)

INFINI = float("inf")


def afficher_separateur():
    # Ligne de séparation pour mieux lire la sortie
    print("\n" + "=" * 60)


def boucle_chemins(L, P):
    # On demande à l'utilisateur s'il veut afficher des chemins
    # Il peut en demander autant qu'il veut, on sort quand il dit non
    n = len(L)

    while True:
        print("\nVoulez-vous afficher un chemin ? (oui / non)")
        reponse = input("  > ").strip().lower()
        # strip() enlève les espaces avant/après la saisie (ex: "  oui  " -> "oui")
        # lower() met tout en minuscules pour accepter "Oui", "OUI", "oui" etc.

        if reponse not in ("oui", "o"):
            print("  Fin de l'affichage des chemins.")
            break

        # On récupère les deux sommets
        try:
            depart = int(input(f"  Sommet de départ (0 à {n - 1}) : ").strip())
            arrivee = int(input(f"  Sommet d'arrivée (0 à {n - 1}) : ").strip())
        except ValueError:
            # ValueError est levée si l'utilisateur tape une lettre à la place d'un nombre
            # ex: int("abc") lève une ValueError, on l'attrape ici pour ne pas planter
            print("  Erreur : veuillez entrer des numéros de sommets valides.")
            continue

        # Les sommets doivent exister dans le graphe
        if not (0 <= depart < n and 0 <= arrivee < n):
            print(f"  Erreur : les sommets doivent être compris entre 0 et {n - 1}.")
            continue

        if depart == arrivee:
            print(f"  Le sommet de départ et d'arrivée sont identiques ({depart}).")
            continue

        distance = L[depart][arrivee]

        # Si la distance est infinie, aucun chemin n'existe entre ces deux sommets
        if distance == INFINI:
            print(f"  Aucun chemin n'existe entre le sommet {depart} et le sommet {arrivee}.")
            continue

        # On reconstruit le chemin grâce à la matrice P
        chemin = obtenir_chemin(P, depart, arrivee)

        if not chemin:
            print(f"  Aucun chemin n'existe entre le sommet {depart} et le sommet {arrivee}.")
        else:
            # join() assemble les éléments de la liste en une seule chaîne
            # ex: [0, 9, 4] -> "0 → 9 → 4"
            # str(s) est nécessaire car join() n'accepte que des chaînes, pas des entiers
            chemin_str = " → ".join(str(s) for s in chemin)
            print(f"\n  Chemin le plus court : {chemin_str}")
            print(f"  Valeur totale        : {distance}")


def traiter_graphe(numero_graphe):
    afficher_separateur()
    print(f"  Traitement du graphe n°{numero_graphe}")
    afficher_separateur()

    # On charge le graphe depuis le fichier txt
    # Si le fichier n'existe pas, charger_graphe retourne None et on s'arrête
    matrice = charger_graphe(numero_graphe)
    if matrice is None:
        return

    # On affiche la matrice avant de lancer l'algorithme
    # pour vérifier que le graphe a bien été lu
    print("\n=== Matrice d'adjacence initiale ===")
    afficher_matrice(matrice, "Matrice initiale")

    # Lancement de Floyd-Warshall
    # L = matrice des distances minimales, P = matrice des prédécesseurs
    print("\n\n=== Exécution de l'algorithme de Floyd-Warshall ===")
    L, P = floyd_warshall(matrice)

    # Affichage de la matrice finale des distances
    afficher_separateur()
    print("=== Matrices finales ===")
    afficher_matrice(L, "L finale (distances minimales)")

    # On vérifie si le graphe contient un circuit absorbant
    # Un circuit absorbant = cycle dont la somme des valeurs est négative
    # Si oui, les distances peuvent décroître à l'infini donc on s'arrête
    afficher_separateur()
    if contient_circuit_absorbant(L):
        print("  ⚠ Le graphe contient au moins un CIRCUIT ABSORBANT.")
        print("  Les chemins les plus courts ne peuvent pas être calculés.")
        return

    print("  ✓ Aucun circuit absorbant détecté.")

    # Tout est bon, on peut afficher les chemins
    afficher_separateur()
    print("=== Recherche de chemins les plus courts ===")
    boucle_chemins(L, P)


def main():
    print("=" * 60)
    print("   Algorithme de Floyd-Warshall — Chemins les plus courts")
    print("=" * 60)

    # Boucle principale : on peut tester plusieurs graphes sans relancer le programme
    while True:
        print("\nEntrez le numéro du graphe à analyser (ou 'quitter' pour terminer) :")
        saisie = input("  > ").strip().lower()

        if saisie in ("quitter", "q"):
            print("\n  Au revoir !")
            break

        # int() convertit la chaîne en entier
        # si l'utilisateur tape autre chose qu'un nombre, ValueError est levée
        try:
            numero = int(saisie)
        except ValueError:
            print("  Erreur : veuillez entrer un numéro de graphe valide.")
            continue

        traiter_graphe(numero)


# Ce bloc garantit que main() ne se lance que si on exécute directement ce fichier
# Si quelqu'un importe ce fichier dans un autre programme, main() ne se lance pas
if __name__ == "__main__":
    main()
