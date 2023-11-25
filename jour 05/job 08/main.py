def my_sort(liste):
    n = len(liste)
    coups_total = 0

    # La boucle extérieure garantit que nous parcourons la liste suffisamment de fois pour trier tous les éléments
    for i in range(n):
        coups = 0  # Initialiser le nombre de coups pour cette itération à 0

        # La boucle intérieure parcourt la liste et effectue les échanges nécessaires
        for j in range(0, n - i - 1):
            # Comparer les éléments adjacents
            if liste[j] > liste[j + 1]:
                # Échanger les éléments s'ils ne sont pas dans l'ordre
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                coups += 1  # Augmenter le nombre de coups

        coups_total += coups  # Ajouter les coups de cette itération au total

        # Si aucun échange n'a été effectué lors de cette itération, la liste est déjà triée
        if coups == 0:
            break

    # Afficher la liste triée et le nombre total de coups nécessaires
    print(f"Liste triée : {liste}")
    print(f"Nombre total de coups nécessaires : {coups_total}")

# Exemple d'utilisation
Liste = [72, 34, 9, 13, 19, 21]
my_sort(Liste)
