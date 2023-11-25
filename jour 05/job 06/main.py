def distance_toilettes_par_semaine(nombre_marches, hauteur_marche_cm):
    jours_par_semaine = 7
    nombre_allers_retours_par_jour = 2

    hauteur_marche_m = hauteur_marche_cm / 100  # Convertir la hauteur de la marche en mètres

    distance_par_aller_retour = nombre_marches * hauteur_marche_m * nombre_allers_retours_par_jour
    distance_par_semaine = distance_par_aller_retour * jours_par_semaine

    return distance_par_semaine

# Exemple d'utilisation
nombre_marches_phare = int(input("Entrez le nombre de marches du phare : "))
hauteur_marche_phare_cm = int(input("Entrez la hauteur de chaque marche en cm : "))

distance_totale = distance_toilettes_par_semaine(nombre_marches_phare, hauteur_marche_phare_cm)

print(f"Pour {nombre_marches_phare} marches de {hauteur_marche_phare_cm} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
