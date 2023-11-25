def afficher_triangle(hauteur):
    # Afficher les lignes du triangle
    for i in range(hauteur):
        # Afficher les espaces avant le caractère '\'
        print(' ' * (hauteur - i - 1), end='')

        # Afficher le caractère '\'
        print('/', end='')

        # Afficher les caractères '_' au milieu du triangle
        if i > 0 and i < hauteur - 1:
            print('_' * (2 * i - 1), end='')

        # Afficher le caractère '/' à la fin de la ligne
        if i != 0:
            print('\\')

# Demander à l'utilisateur la hauteur du triangle
hauteur_triangle = int(input("Entrez la hauteur du triangle : "))

# Afficher le triangle
afficher_triangle(hauteur_triangle)
