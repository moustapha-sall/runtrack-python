def my_long_word(longueur_minimale, phrase):
    mots = phrase.split()  # Diviser la phrase en une liste de mots
    mots_filtres = []

    for mot in mots:
        if len(mot) > longueur_minimale:
            mots_filtres.append(mot)

    resultat = " ".join(mots_filtres)  # Joindre les mots filtrés en une chaîne
    return resultat

# Exemple d'utilisation
chiffre = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(chiffre, phrase)
print("Output :", resultat)
