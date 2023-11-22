def afficher_produits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucun produit correspondant.")

# Exemple d'utilisation
afficher_produits("fruits", "hiver")  # Affichera "Orange, mandarine et kiwi"
afficher_produits("fruits", "ete")    # Affichera "Poire, fraise, cassis"
afficher_produits("legume", "hiver")  # Affichera "Carotte, topinambour, endive"
afficher_produits("legume", "ete")    # Affichera "Artichaut, aubergine, navet"
afficher_produits("pigeon", "ete")   # Affichera "Aucun produit correspondant."
