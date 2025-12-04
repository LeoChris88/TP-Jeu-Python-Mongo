from time import time
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
    time.sleep(0.5)

def pause_normal():
    time.sleep(1.5)

def calcul_degats(atk, defense):
    d = atk - (defense * 0.5)
    if d < 0:
        d = 0
    return int(d)

if __name__ == "__main__":
    db = get_db()
    print("Connexion BDD OK\n")

    print("Test pour récuperer un monstre aléatoire :")
    m = get_random_monster(db)
    print(" -> Monstre tiré :", m)

    print("\nTest calcul degats :")
    print("20 atk vs 8 def =", calcul_degats(20, 8))
    print("10 atk vs 40 def =", calcul_degats(10, 40))