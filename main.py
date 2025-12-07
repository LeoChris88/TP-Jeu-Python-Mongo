from db_init import personnages, monstres
from game import choix_personnage, combat_test
from utils import get_db, get_random_monster
from models import Personnage, Monstre

if __name__ == "__main__":
    db = get_db()
    monstre_data = get_random_monster(db)

    if monstre_data is None:
        print("Erreur : aucun monstre dans la BDD.")
    else:
        persos_db = [
    Personnage(p["name"], p["atk"], p["defn"], p["pv"])
    for p in personnages
    ]
        team = choix_personnage(persos_db)

        monstre_test = Monstre(
            monstre_data["name"],
            monstre_data["atk"],
            monstre_data["def"],
            monstre_data["pv"]
        )

        print("Monstre choisi pour le combat :", monstre_test.name, "[", monstre_test.atk, "atk", monstre_test.defn, "def", monstre_test.pv, "pv]")
        combat_test(team, monstre_test)