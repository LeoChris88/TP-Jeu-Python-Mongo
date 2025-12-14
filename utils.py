import time
from pymongo import MongoClient
import random

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["jeu_python"]
    return db

def debug(msg):
    print("[DEBUG] ", msg)

def get_random_monster(db):
    monstres = list(db["monstres"].find({}))
    if len(monstres) == 0:
        debug("Pas de monstres dans la bdd")
        return None
    
    monstre = random.choice(monstres)
    return monstre

def pause_rapide():
    time.sleep(0.5)

def pause_normal():
    time.sleep(1.5)
        
def narration_debut_combat(team):
    print("=== DEBUT COMBAT ===")
    for p in team:
        print(f"- {p.name} ({p.atk} atk / {p.defn} def / {p.pv} pv)")
        pause_normal()

def narration_nouvelle_vague(monstre):
    print(f"\n>> Le monstre {monstre.name} est vaincu !")
    print("\n=== FIN DE LA VAGUE ===")
    print("\n=== UNE NOUVELLE VAGUE ARRIVE... ===")

def scores_bdd(limit=3):
    db = get_db()
    collection = db["scores"]
    return list(
        collection.find()
        .sort("score", -1)
        .limit(limit)
    )

def sauvegarde_scores(pseudo, vague):
    db = get_db()
    collection = db["scores"]

    collection.insert_one({
        "player": pseudo,
        "score": vague
    })

def afficher_scores():
    print("\n=== CLASSEMENT DES JOUEURS ===\n")

    scores = scores_bdd(3)

    if not scores:
        print("Aucun score enregistré pour le moment.")
        return

    for i, s in enumerate(scores, start=1):
        joueur = s.get("player", "Inconnu")
        vagues = s.get("score", 0)
        print(f"{i}) {joueur} - {vagues} vagues")

def calcul_degats(atk, defense):
    d = atk - (defense * 0.5)
    if d < 0:
        d = 0
    return int(d)

def message_defaite(vague):
    print("La team a été vaincue !")
    print("=== T'AS LOOSE SALE BOT ===")
    print(f"=== TU AS SURVÉCU {vague} VAGUE(S) ===")

def menu_fin_partie():
    print("\n1) Rejouer")
    print("2) Quitter")

    choix = input("Votre choix : ")
    while choix not in ["1", "2"]:
        choix = input("Choisissez 1 ou 2 : ")

    return choix

def buff_monstre(monstre, vague):
    monstre.pv = int(monstre.pv * (1 + 0.1 * (vague - 1)))
    monstre.atk = int(monstre.atk * (1 + 0.05 * (vague - 1)))

def buff_perso():
    print("1) +5 ATK pour toute la team")
    print("2) +5 DEF pour toute la team")
    print("3) +20 PV max pour toute la team")

    choix = input("Votre choix : ")
    while choix not in ["1", "2", "3"]:
        choix = input("Votre choix : ")

    return choix

def appliquer_bonus(team, choix):
    for p in team:
        if choix == "1":
            p.atk += 5
        elif choix == "2":
            p.defn += 5
        elif choix == "3":
            p.pv += 20
            p.pv_max += 20