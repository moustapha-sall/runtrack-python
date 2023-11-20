# Initialisation des variables
montant_initial = 10000  # Montant initial de l'investissement en euros
taux_rendement_annuel = 5  # Taux de rendement annuel en pourcentage

# Affichage du gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros")

# Augmentation du capital de 5 000 euros et du taux de rendement de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Nouveau gain annuel après augmentation : {nouveau_gain_annuel} euros")

# Retrait de 10% du montant total et diminution du rendement de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement
montant_final = montant_initial + nouveau_gain_annuel

# Affichage du nouveau gain après retrait
nouveau_gain_final = (taux_rendement_annuel / 100) * montant_final
print(f"Montant final de l'investissement : {montant_final} euros")
print(f"Nouveau gain après retrait : {nouveau_gain_final} euros")
