def arrondir_notes(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            # Si la note est inférieure à 40, l'étudiant échoue et la note reste inchangée
            notes_arrondies.append(note)
        else:
            # Calculer le prochain multiple de 5 supérieur ou égal à la note
            multiple_de_5_superieur = (note // 5 + 1) * 5
            
            # Vérifier si l'arrondi est nécessaire
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_etudiants = [83, 75, 42, 37, 91, 105, 103]
notes_arrondies = arrondir_notes(notes_etudiants)

print(f"Notes originales : {notes_etudiants}")
print(f"Notes arrondies : {notes_arrondies}")
