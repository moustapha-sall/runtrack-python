def determiner_developpeur(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Exemple d'utilisation
determiner_developpeur("JavaScript")  # Affichera "Tu es un développeur web"
determiner_developpeur("python")      # Affichera "Tu es un développeur IA"
determiner_developpeur("java")        # Affichera "Tu es un développeur logiciel"
determiner_developpeur("reactjs")     # Affichera "Tu es un développeur mobile"
determiner_developpeur("C++")         # Affichera "Un jour, je serai le meilleur développeur..."
