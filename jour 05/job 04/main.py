def afficher_tapis_diagonale(taille):
    for i in range(taille + 1):
        for j in range(taille + 1):
            # Si nous sommes sur la diagonale, afficher un caractère différent
            if i == j:
                print('\\', end=' ')
            else:
                print('-', end=' ')
        print()  # Aller à la ligne après chaque ligne du tapis

# Demander à l'utilisateur la taille du tapis
taille_tapis = int(input("Entrez la taille du tapis : "))

# Afficher le tapis avec la diagonale
afficher_tapis_diagonale(taille_tapis)
