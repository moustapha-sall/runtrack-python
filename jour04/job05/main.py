def modifier_liste(liste):
    # Afficher la deuxième valeur de la liste
    deuxieme_valeur = liste[1]
    print("Deuxième valeur de la liste :", deuxieme_valeur)

    # Remplacer L[3] par la somme des cases voisines L[2] & L[4]
    liste[3] = liste[2] + liste[4]

    # Afficher le tableau après la modification
    print("Liste après la modification :", liste)

    # Afficher la dernière valeur de la liste
    derniere_valeur = liste[-1]
    print("Dernière valeur de la liste :", derniere_valeur)

# Créer une liste d'au moins 5 entiers
L = [1, 2, 3, 4, 5]

# Appeler la fonction pour effectuer les opérations
modifier_liste(L)
