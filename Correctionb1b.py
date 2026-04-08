# Commentaire Algo FR
# TESTER-CERVEAU
# Traduire en python


from main import Choix1


def demander_age_utilisateur():
    
    # Tant que age n'est pas un nombre
    while True: 
    # Demander age
        age = input("entrez votre age :")
    # si age est un nombre
        if age.isdigit():
        # -----renvoyer age
            return int(age)
    # sinon
    # ----afficher message d'erreur
        print("Veuillez entrer un nombre valide pour votre age.")

demander_age_utilisateur()




 