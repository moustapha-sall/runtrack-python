def type_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilatéral"
        elif a == b or b == c or a == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Rectangle et Isocèle"
            else:
                return "Isocèle"
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle"
        else:
            return "Quelconque"
    else:
        return "Impossible de former un triangle"

# Demander à l'utilisateur trois longueurs
try:
    a = float(input("Entrez la longueur a : "))
    b = float(input("Entrez la longueur b : "))
    c = float(input("Entrez la longueur c : "))
except ValueError:
    print("Veuillez entrer des valeurs numériques.")
    exit()

# Déterminer le type de triangle
resultat = type_triangle(a, b, c)

# Afficher le résultat
print(f"Pour les longueurs a={a}, b={b}, c={c} : {resultat}")
