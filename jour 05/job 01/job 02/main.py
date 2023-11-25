def afficher_rectangle(width, height):
    # Afficher la première ligne avec des '-'
    print('-' * width)

    # Afficher les lignes du milieu avec '|'
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Afficher la dernière ligne avec des '-'
    if height > 1:
        print('-' * width)

# Demander à l'utilisateur les dimensions du rectangle
largeur = int(input("Entrez la largeur du rectangle : "))
hauteur = int(input("Entrez la hauteur du rectangle : "))

# Afficher le rectangle
afficher_rectangle(largeur, hauteur)
