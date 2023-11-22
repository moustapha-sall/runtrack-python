def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Vérification pour éviter la division par zéro
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro n'est pas autorisée."
    elif operator == '%':
        # Vérification pour éviter le modulo par zéro
        if num2 != 0:
            return num1 % num2
        else:
            return "Le modulo par zéro n'est pas autorisé."
    else:
        return "Opérateur non valide."

# Exemples d'appels de la fonction
result_addition = calcule(4, '+', 6)
result_subtraction = calcule(8, '-', 2)
result_multiplication = calcule(3, '*', 5)
result_division = calcule(11, '/', 3)
result_modulo = calcule(5, '%', 4)

# Affichage des résultats
print("Addition:", result_addition)
print("Soustraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
print("Modulo:", result_modulo)
