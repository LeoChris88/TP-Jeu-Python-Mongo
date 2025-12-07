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
        debug("Pas de monstres dans la bdd (??)")
        return None
    
    monstre = random.choice(monstres)
    return monstre

def pause_rapide():
    time.sleep(0.5) #mais là le probleme c'e

def pause_normal():
    time.sleep(1.5)

def narration_nouvelle_vague(monstre):
    print(f"\n>> Le monstre {monstre.name} est vaincu !")
    print("\n=== FIN DE LA VAGUE ===")
    print("\n=== UNE NOUVELLE VAGUE ARRIVE... ===")

def calcul_degats(atk, defense):
    d = atk - (defense * 0.5)
    if d < 0:
        d = 0
    return int(d)

def message_defaite(vague):
    print("La team a été vaincue !")
    print("=== T'AS LOOSE SALE BOT ===")
    print(f"=== TU AS SURVÉCU {vague} VAGUE(S) ===")
