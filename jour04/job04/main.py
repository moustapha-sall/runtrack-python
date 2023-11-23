def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")
    return fruits

# Appel de la fonction et affichage du résultat
liste_fruits = ajouter_mangue()
print(liste_fruits)
