from pymongo import MongoClient

db_client = MongoClient('mongodb://localhost:27017/')
db = db_client['jeu_python']

personnages = [
    {"name": "Guerrier", "atk": 15, "defn": 10, "pv": 100},
    {"name": "Mage", "atk": 20, "defn": 5, "pv": 80},
    {"name": "Archer", "atk": 18, "defn": 7, "pv": 90},
    {"name": "Voleur", "atk": 22, "defn": 8, "pv": 85},
    {"name": "Paladin", "atk": 14, "defn": 12, "pv": 110},
    {"name": "Sorcier", "atk": 25, "defn": 3, "pv": 70},
    {"name": "Chevalier", "atk": 17, "defn": 15, "pv": 120},
    {"name": "Moine", "atk": 19, "defn": 9, "pv": 95},
    {"name": "Berserker", "atk": 23, "defn": 6, "pv": 105},
    {"name": "Chasseur", "atk": 16, "defn": 11, "pv": 100},
]

monstres = [
    {"name": "Gobelin", "atk": 10, "defn": 5, "pv": 50},
    {"name": "Orc", "atk": 20, "defn": 8, "pv": 120},
    {"name": "Dragon", "atk": 35, "defn": 20, "pv": 300},
    {"name": "Zombie", "atk": 12, "defn": 6, "pv": 70},
    {"name": "Troll", "atk": 25, "defn": 15, "pv": 200},
    {"name": "Spectre", "atk": 18, "defn": 10, "pv": 100},
    {"name": "Golem", "atk": 30, "defn": 25, "pv": 250},
    {"name": "Vampire", "atk": 22, "defn": 12, "pv": 150},
    {"name": "Loup-garou", "atk": 28, "defn": 18, "pv": 180},
    {"name": "Squelette", "atk": 15, "defn": 7, "pv": 90},
]

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["jeu_python"]

    personnages_col = db["personnages"]
    monstres_col = db["monstres"]
    scores_col = db["scores"]

    personnages_col.delete_many({})
    monstres_col.delete_many({})
    scores_col.delete_many({})

    personnages_col.insert_many(personnages)
    monstres_col.insert_many(monstres)

    scores_col.create_index([("score", -1)])

    print(f"Initialisation terminée dans la BDD '{'jeu_python'}'.")
    
    print(f"{monstres_col.count_documents({})} monstres insérés.")
    print("Collection 'scores' prête.")

if __name__ == "__main__":
    main()