def check_positivity(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("Le nombre est nul")

# Appels de la fonction avec différents paramètre
check_positivity(-8)
check_positivity(-4)
check_positivity(0)
check_positivity(12)
