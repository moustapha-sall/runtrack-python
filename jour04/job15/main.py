def tri_bulles(liste):
    n = len(liste)

    # Tri à bulles
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

def arrondir_liste(liste):
    # Arrondir chaque nombre de la liste
    for i in range(len(liste)):
        liste[i] = int(liste[i] + 0.5)  # Conversion float -> int avec arrondi

# Liste initiale
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres
arrondir_liste(ma_liste)

# Trier la liste arrondie
tri_bulles(ma_liste)

# Afficher le résultat
print("Liste arrondie et triée :", ma_liste)
