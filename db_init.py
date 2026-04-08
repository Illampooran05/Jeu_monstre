# importe mes modèles 
from pymongo import MongoClient

#Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["jeumonstre"]

#Les 3 collections
collection_personnages = db["personnages"]
collection_monstres    = db["monstres"]
collection_scores      = db["scores"]

from models import list_Personnage, list_monstre

# connecter à la base de données
from datetime import datetime




# Fonction pour charger les scores depuis MongoDB
def charger_scores():
    try:
        return list(collection_scores.find({}, {'_id': 0}).sort('points', -1))
    except Exception:
        return []

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
    """Sauvegarde le score d'un joueur dans MongoDB"""
    nouveau_score = {
        'nom': nom_joueur,
        'points': points,
        'date': datetime.now().strftime('%d/%m/%Y %H:%M')
    }
    try:
        collection_scores.insert_one(nouveau_score)
        print(f"Score de {nom_joueur} ({points} points) sauvegardé !")
    except Exception:
        print("Impossible de sauvegarder le score. Vérifiez la connexion à la base de données.")

def main():
    init_db()  # Appeler la fonction d'initialisation de la base de données
    print("Base de données initialisée avec succès !")
    afficher_scores()  # Appeler la fonction pour afficher les scores (à implémenter)

if __name__ == "__main__":
    main()


 
     

