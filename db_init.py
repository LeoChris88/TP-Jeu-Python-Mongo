from pymongo import MongoClient

db_client = MongoClient('mongodb://localhost:27017/')
db = db_client['jeu_video']

personages = [
    {"name": "Guerrier", "atk": 15, "def": 10, "pv": 100},
    {"name": "Mage", "atk": 20, "def": 5, "pv": 80},
    {"name": "Archer", "atk": 18, "def": 7, "pv": 90},
    {"name": "Voleur", "atk": 22, "def": 8, "pv": 85},
    {"name": "Paladin", "atk": 14, "def": 12, "pv": 110},
    {"name": "Sorcier", "atk": 25, "def": 3, "pv": 70},
    {"name": "Chevalier", "atk": 17, "def": 15, "pv": 120},
    {"name": "Moine", "atk": 19, "def": 9, "pv": 95},
    {"name": "Berserker", "atk": 23, "def": 6, "pv": 105},
    {"name": "Chasseur", "atk": 16, "def": 11, "pv": 100},
]

monstres = [
    {"name": "Gobelin", "atk": 10, "def": 5, "pv": 50},
    {"name": "Orc", "atk": 20, "def": 8, "pv": 120},
    {"name": "Dragon", "atk": 35, "def": 20, "pv": 300},
    {"name": "Zombie", "atk": 12, "def": 6, "pv": 70},
    {"name": "Troll", "atk": 25, "def": 15, "pv": 200},
    {"name": "Spectre", "atk": 18, "def": 10, "pv": 100},
    {"name": "Golem", "atk": 30, "def": 25, "pv": 250},
    {"name": "Vampire", "atk": 22, "def": 12, "pv": 150},
    {"name": "Loup-garou", "atk": 28, "def": 18, "pv": 180},
    {"name": "Squelette", "atk": 15, "def": 7, "pv": 90},
]

def main():
    client = MongoClient('mongodb://localhost:27017/')
    db = client["jeu_video"]

    personnages_col = db["personnages"]
    monstres_col = db["monstres"]
    scores_col = db["scores"]

    personnages_col.delete_many({})
    monstres_col.delete_many({})
    scores_col.delete_many({})

    personnages_col.insert_many(personnages)
    monstres_col.insert_many(monstres)

    scores_col.create_index([("score", -1)])

    print(f"Initialisation terminée dans la BDD '{'jeu_video'}'.")
    print(f"{personnages_col.count_documents({})} personnages insérés.")
    print(f"{monstres_col.count_documents({})} monstres insérés.")
    print("Collection 'scores' prête.")

if __name__ == "__main__":
    main()