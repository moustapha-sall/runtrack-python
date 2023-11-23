# Définir la liste
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Récupérer la valeur, le maximum et le minimum
valeur = L[0]  # On initialise avec la première valeur de la liste
maximum = max(L)
minimum = min(L)

# Parcourir la liste pour récupérer la valeur
for nombre in L:
    # Mettre à jour la valeur si on trouve un élément plus grand
    if nombre > valeur:
        valeur = nombre

# Afficher les résultats
print("La valeur maximale dans la liste est :", maximum)
print("La valeur minimale dans la liste est :", minimum)
