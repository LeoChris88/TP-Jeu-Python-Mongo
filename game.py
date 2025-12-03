# game.py (debut)
import array
from utils import get_db, get_random_monster, calcul_degats
from models import Personnage, Monstre
from db_init import personnages, monstres
import time

def get_valid_int(message, max_choice):
    while True:
        try:
            value = int(input(message))
            if 1 <= value <= max_choice:
                return value
            print(f"Veuillez entrer une valeur entre 1 et {max_choice}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def choix_personnage(personnages):
    team = []
    print("=== BIENVENUE DANS LE JEU PYTHON MONGO ===\n")
    time.sleep(1)
    print("=== COMPOSEZ VOTRE TEAM (3 personnages) ===")
    time.sleep(1)
    print("Liste des personnages disponibles :\n")
    time.sleep(1)
    liste = ["Guerrier", "Mage", "Archer", "Voleur", "Paladin", "Sorcier", "Chevalier", "Moine", "Berserker", "Chasseur"] # tu utilise la db
    print(liste)

    while len(team) < 3:
        choice = get_valid_int(f"Choisissez un personnage en tapant un nombre entre 1 et {len(liste)}:", len(liste))
        if choice not in range(1, 11):
            print("Choix invalide, veuillez réessayer.")
            return choix_personnage(personnages)
        team.append(personnages[choice - 1])
        liste.remove(liste[choice - 1])
    for p in team:
        print(f"- {p.name}")
    print("\n=== TEAM VALIDÉE ===")

def combat_test(team, monstre):
    print("=== DEBUT COMBAT ===")
    print(f"{team[0].name} VS {monstre.name}")
    print("--------------------")

    tour = 1

    while team.est_vivant() and monstre.est_vivant():
        print(f"\n--- TOUR {tour} ---")

        dmg_perso = calcul_degats(team[0].atk, monstre.defn)
        monstre.subir_degats(dmg_perso)
        print(f"{team[0].name} attaque ({dmg_perso} dmg) -> {monstre.pv} pv reste")

        if not monstres.est_vivant():
            print(f"\n>> Le monstre {monstre.name} est vaincu !")
            break
        if team[0].pv <= 0:
            print(f"\n>> Le personnage {team[0].name} est vaincu !")
            break
        dmg_monstre = monstre.attaquer(team[0])
        print(f"{monstre.name} riposte ({dmg_monstre} dmg) -> {team[0].pv} pv reste")
        tour += 1

    print("\n=== FIN DU COMBAT ===\n")


if __name__ == "__main__":
    db = get_db()
    monstre_data = get_random_monster(db)

    if monstre_data is None:
        print("Erreur : aucun monstre dans la BDD.")
    else:
        choix_personnage([])

        monstre_test = Monstre(
            monstre_data["name"],
            monstre_data["atk"],
            monstre_data["def"],
            monstre_data["pv"]
        )

        print("Monstre choisi pour le combat :", monstre_test.name, "[", monstre_test.atk, "atk", monstre_test.defn, "def", monstre_test.pv, "pv]")
        combat_test(choix_personnage, monstre_test)