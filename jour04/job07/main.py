# Définir la liste
L = [8, 24, 48, 2, 16]

# Initialiser le compteur
nombre_multiples_de_3 = 0

# Parcourir la liste
for nombre in L:
    # Vérifier si le nombre est un multiple de 3
    if nombre % 3 == 0:
        # Incrémenter le compteur
        nombre_multiples_de_3 += 1

# Afficher le résultat
print("Le nombre de multiples de 3 dans la liste est :", nombre_multiples_de_3)
