# importe mes modèles 
from models import list_Personnage, list_monstre

# connecter à la base de données (version fichier JSON pour simplifier)
import json
import os
from datetime import datetime

# Fichier pour stocker les scores
SCORES_FILE = 'scores.json'

# Fonction pour charger les scores depuis le fichier
def charger_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

# Fonction pour sauvegarder les scores dans le fichier
def sauvegarder_scores(scores):
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, indent=2, default=str)

# créer les tables pour mes modèles


def init_db():
    # Les listes sont déjà définies dans models.py
    pass

def afficher_scores():
    """Affiche les 3 meilleurs scores"""
    print("\n" + "="*40)
    print("🏆 MEILLEURS SCORES 🏆")
    print("="*40)
    
    scores = charger_scores()
    
    if not scores:
        print("Aucun score enregistré pour le moment.")
        print("Jouez une partie pour apparaître dans le classement !")
        return
    
    # Trier les scores par points décroissants et prendre les 3 premiers
    meilleurs_scores = sorted(scores, key=lambda x: x.get('points', 0), reverse=True)[:3]
    
    # Afficher les scores
    for i, score in enumerate(meilleurs_scores, 1):
        nom = score.get('nom', 'Anonyme')
        points = score.get('points', 0)
        date = score.get('date', 'N/A')
        
        print(f"{i}. {nom:<15} | {points:>3} points | {date}")
    
    print("="*40)

def sauvegarder_score(nom_joueur, points):
    """Sauvegarde le score d'un joueur dans le fichier JSON"""
    scores = charger_scores()
    
    nouveau_score = {
        'nom': nom_joueur,
        'points': points,
        'date': datetime.now().strftime('%d/%m/%Y %H:%M')
    }
    
    scores.append(nouveau_score)
    sauvegarder_scores(scores)
    print(f"Score de {nom_joueur} ({points} points) sauvegardé !")

def main():
    init_db()  # Appeler la fonction d'initialisation de la base de données
    print("Base de données initialisée avec succès !")
    afficher_scores()  # Appeler la fonction pour afficher les scores (à implémenter)

if __name__ == "__main__":
    main()


 
     

