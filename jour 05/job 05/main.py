def decaler_message(message, decalage):
    resultat = ""
    
    for caractere in message:
        # Vérifier si le caractère est une lettre de l'alphabet
        if caractere.isalpha():
            # Déterminer la casse (majuscule ou minuscule)
            est_majuscule = caractere.isupper()
            
            # Décaler le caractère dans l'alphabet
            code_ascii = ord(caractere)
            nouveau_code_ascii = (code_ascii - ord('A' if est_majuscule else 'a') + decalage) % 26
            nouveau_caractere = chr(nouveau_code_ascii + ord('A' if est_majuscule else 'a'))
            
            # Ajouter le caractère décalé au résultat
            resultat += nouveau_caractere
        else:
            # Si le caractère n'est pas une lettre, le laisser tel quel
            resultat += caractere
    
    return resultat

# Exemple d'utilisation
message_original = "Good Morning!"
decalage_utilisateur = 3
message_decale = decaler_message(message_original, decalage_utilisateur)

print(f"Message original: {message_original}")
print(f"Message décalé de {decalage_utilisateur} positions: {message_decale}")
