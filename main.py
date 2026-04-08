
from db_init import afficher_scores
import game
from models import list_Personnage, list_monstre
 

# initilier la base de données
def afficher_header(text: str):
    print("-"*50)
    print(text.center(50))
    print("-"*50)
    

#afficher les choix 
Choix1 = "Nouvelle partie"
Choix2 = "afficher les trois meilleurs scores" 
Choix3 = "Quitter"

def afficher_menu():
     # Afficher MON EN tete
    titre = "Jeu de combat de monstres"
    afficher_header(titre)
     #afficher les choix de partie
    print("1. " + Choix1)
    print("2. " + Choix2)
    print("3. " + Choix3)

def recuperer_choix_utilisateur():
    while True:
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
        if choix in ['1', '2', '3']:
            choix = int(choix)
            if choix == 1:
                print(f"Vous avez choisi : {Choix1}")
            elif choix == 2:
                print(f"Vous avez choisi : {Choix2}")
            else:
                print(f"Vous avez choisi : {Choix3}")
            return choix
        else:
            print("Veuillez entrer un choix valide (1, 2 ou 3).")



def creer_equipe_utilisateur():
    print("Création de votre équipe de personnages.")
    equipe = []
    for i in range(3):
        print(f"Choisissez le personnage {i+1} :")
        for index, personnage in enumerate(list_Personnage):
            print(f"{index + 1}. {personnage['name']} (ATK: {personnage['ATK']}, DEF: {personnage['DEF']}, PV: {personnage['PV']})")
        while True:
            choix = input("Entrez le numéro du personnage que vous souhaitez ajouter à votre équipe : ")
            if choix.isdigit() and 1 <= int(choix) <= len(list_Personnage):
                equipe.append(list_Personnage[int(choix) - 1])
                break
            else:
                print("Veuillez entrer un numéro valide.")
    return equipe

def créer_equipe_monstre():
    # Créer une équipe de monstres aléatoire pour le combat
    import random
    equipemonstre = random.sample(list_monstre, 3)
    print("L'équipe de monstres a été créée ! Voici les monstres que vous allez affronter :")
    for monstre in equipemonstre:
        print(f"- {monstre['name']} (ATK: {monstre['ATK']}, DEF: {monstre['DEF']}, PV: {monstre['PV']})")   
    return equipemonstre



def jouer():
    print("Lancement de la nouvelle partie...")
    #choix du nom de l'utilisateur
    nom = input("Entrez votre nom : ")
    print(f"Bienvenue, {nom} ! Créons votre équipe de personnages.")
    #   créer l'équipe de l'utilisateur
    equipe = creer_equipe_utilisateur()
    print("Votre équipe est prête ! Voici les personnages que vous avez choisis :")
    for personnage in equipe:
        print(f"- {personnage['name']} (ATK: {personnage['ATK']}, DEF: {personnage['DEF']}, PV: {personnage['PV']})")

    #   créer l'équipe de monstres
    equipemonstre = créer_equipe_monstre()
    print("Préparez-vous pour le combat contre les monstres !")

    #   lancer les combats (à implémenter dans game.py)
    points = game.lancer_combat(equipe, equipemonstre, nom)
    
    if points > 0:
        print(f"Félicitations {nom} ! Vous avez terminé la partie avec {points} points.")
    else:
        print(f"Dommage {nom}, vous avez perdu cette partie. Réessayez !")




def lancer_option(choix):
    #  démarrer une nouvelle partie
    if choix == 1:
        jouer()  # Appeler la fonction pour démarrer le jeu
       
    elif choix == 2:
        print("Affichage des trois meilleurs scores...")
        afficher_scores()  # Appeler la fonction pour afficher les scores (à implémenter)


     #   quitter le jeu    
    elif choix == 3:
        print("Quitter le jeu. Au revoir!")

 

    

def main():
    afficher_menu()

    # recuperer le choix de l'utilisateur
    choix = recuperer_choix_utilisateur()

    # lance la bonne option en fonction du choix de l'utilisateur
    lancer_option(choix)

if __name__ == "__main__":

    main()