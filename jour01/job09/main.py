# Initialisation des variables du produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0  # Prix unitaire en euros
quantite_en_stock = 50

# Affichage des informations du produit
print(f"Informations sur le produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock} unités")

# Ajout de produits en stock
quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
quantite_en_stock += quantite_achetee

# Mise à jour du prix unitaire après l'inflation
prix_unitaire *= 1.10  # Augmentation de 10%

# Affichage des nouvelles informations sur le produit
print("\nInformations mises à jour sur le produit :")
print(f"Prix unitaire après inflation : {prix_unitaire} euros")
print(f"Nouvelle quantité en stock : {quantite_en_stock} unités")
