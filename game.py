# 3: Gestion des combats (game.py)
        #gérant la logique du combat.
# 3.1 Lancer les vagues de combat
# 3.1.1 
# 3.2 Terminer les combats et stocker le score



     

#- Chaque personnage de l'équipe attaque le monstre et réduit ses PV en fonction de l'attaque et de la défense.
import random

from main import afficher_menu


def attaque_équipe(equipe, equipemonstre):
    for personnage in equipe:
        if personnage['PV'] > 0:  # Vérifie si le personnage est encore en vie
            monstre_cible = random.choice(equipemonstre)  # Choisit un monstre aléatoire
            if monstre_cible['PV'] > 0:  # Vérifie si le monstre cible est encore en vie
                dégâts = max(0, personnage['ATK'] - monstre_cible['DEF'])  # Calcule les dégâts infligés
                monstre_cible['PV'] -= dégâts  # Réduit les PV du monstre cible
                print(f"{personnage['name']} attaque {monstre_cible['name']} et inflige {dégâts} dégâts !") 




#- Le monstre attaque un personnage aléatoire de l'équipe et inflige des dégâts.
def attaque_monstre(equipe, equipemonstre):
    for monstre in equipemonstre:
        if monstre['PV'] > 0:  # Vérifie si le monstre est encore en vie
            personnage_cible = random.choice(equipe)  # Choisit un personnage aléatoire
            if personnage_cible['PV'] > 0:  # Vérifie si le personnage cible est encore en vie
                dégâts = max(0, monstre['ATK'] - personnage_cible['DEF'])  # Calcule les dégâts infligés
                personnage_cible['PV'] -= dégâts  # Réduit les PV du personnage cible
                print(f"{monstre['name']} attaque {personnage_cible['name']} et inflige {dégâts} dégâts !")


#- Combat automatisé où les personnages et les monstres s'affrontent jusqu'à ce que l'un des deux camps soit complètement vaincu.
def Combat_automatisé(equipe, equipemonstre):
    while any(p['PV'] > 0 for p in equipe) and any(m['PV'] > 0 for m in equipemonstre):
        attaque_équipe(equipe, equipemonstre)  # Les personnages attaquent les monstres
        attaque_monstre(equipe, equipemonstre)  # Les monstres attaquent les personnages

    if all(p['PV'] <= 0 for p in equipe):
        print("Les monstres ont gagné le combat !")
    else:
        print("Votre équipe a gagné le combat !")

        

def lancer_combat(equipe, equipemonstre, nom):
    print("Le combat commence !")
    
    Combat_automatisé(equipe, equipemonstre)
    
    # Calculer les points basés sur les PV restants de l'équipe
    points = sum(p['PV'] for p in equipe if p['PV'] > 0)
    
    # Sauvegarder le score
    from db_init import sauvegarder_score
    sauvegarder_score(nom, points)
    
    return points

    # afficher les menu et les options de combat
    afficher_menu() 




     
     