# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# Initialiser la somme
somme_valeurs_paires = 0

# Parcourir la liste
for nombre in L:
    # Vérifier si le nombre est pair
    if nombre % 2 == 0:
        # Ajouter le nombre à la somme
        somme_valeurs_paires += nombre

# Afficher le résultat
print("La somme des valeurs paires dans la liste est :", somme_valeurs_paires)
