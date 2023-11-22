def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0 and minutes_restantes == 0:
            print("0 heures et 0 minutes")
        elif heures == 0:
            print(f"{minutes_restantes} minutes")
        elif minutes_restantes == 0:
            print(f"{heures} heures")
        else:
            print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Le nombre de minutes doit être un entier positif.")

# Exemples d'utilisation
time_to_text(160)   # Affichera "2 heures 40 minutes"
