# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit
produit = 1

# Parcourir la liste
for nombre in L:
    # Vérifier si le nombre est dans l'intervalle [25, 90]
    if 25 <= nombre <= 90:
        # Multiplier le nombre avec le produit actuel
        produit *= nombre

# Afficher le résultat
print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)
