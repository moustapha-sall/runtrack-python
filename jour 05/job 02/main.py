def afficher_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne : afficher une ligne complète de '-'
            print('-' * width)
        else:
            # Lignes intermédiaires : afficher '|' aux extrémités et des espaces à l'intérieur
            print('|' + ' ' * (width - 2) + '|')

# Demander à l'utilisateur de saisir la largeur et la hauteur
width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))

# Appeler la fonction pour afficher le rectangle
afficher_rectangle(width, height)
