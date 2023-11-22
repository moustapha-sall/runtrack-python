def verifier_pair_impair(nombre):
    # Vérifier si le nombre est un chiffre entier et positif
    if isinstance(nombre, int) and nombre >= 0:
        # Vérifier si le nombre est pair ou impair
        if nombre % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Le nombre doit être un chiffre entier et positif."

# Appeler la fonction avec différentes valeurs
resultat1 = verifier_pair_impair(10)
print("10 est", resultat1)

resultat2 = verifier_pair_impair(7)
print("7 est", resultat2)

resultat3 = verifier_pair_impair(15)
print("15 est", resultat3)

resultat4 = verifier_pair_impair(-3)
print("-3 est", resultat4)

resultat5 = verifier_pair_impair("abc")
print("'abc' est", resultat5)
