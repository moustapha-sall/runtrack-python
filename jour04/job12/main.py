def tri_bulles(liste):
    n = len(liste)

    # Parcourir tous les éléments de la liste
    for i in range(n):
        # La dernière i-ème position est déjà triée, on la laisse de côté
        for j in range(0, n-i-1):
            # Échanger si l'élément trouvé est plus grand que le suivant
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]


L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print("Liste non triée :", L)

# Appeler la fonction de tri
tri_bulles(L)

print("Liste triée :", L)
