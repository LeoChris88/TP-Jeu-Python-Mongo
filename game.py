# game.py (debut)
import array
import random
from utils import get_db, get_random_monster, calcul_degats, pause_rapide, pause_normal, narration_nouvelle_vague
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
def afficher_menu_choix():
    print("=== BIENVENUE DANS LE JEU PYTHON MONGO ===\n")
    pause_normal()
    print("=== COMPOSEZ VOTRE TEAM (3 personnages) ===")
    pause_normal()
    print("Liste des personnages disponibles :\n")
    pause_normal()

def afficher_team(team):
    for p in team:
        print(f"- {p.name}")
        pause_rapide()
def affcher_ajout_perso_restant(perso_restant):
    print("Personnage ajouté")
    print("Choix Restant :")
    for p in perso_restant:
        print(f"- {p}")
    
def choix_personnage(personnages):
    team = []
    liste = ["Guerrier", "Mage", "Archer", "Voleur", "Paladin", "Sorcier", "Chevalier", "Moine", "Berserker", "Chasseur"]
    afficher_menu_choix()
    print(liste)
    
    while len(team) < 3:
        choice = get_valid_int(f"Choisissez un personnage en tapant un nombre entre 1 et {len(liste)} :", len(liste))
        perso = personnages.pop(choice - 1)
        team.append(perso)
    
    afficher_team(team)
    print("\n=== TEAM VALIDÉE ===")
    return team 

def combat_detail(tour, monstre, team):
    pause_normal()
    print(f"\n--- TOUR {tour} ---")

    for p in team:
        if p.est_vivant():
            dmg_perso = max(0, p.atk - monstre.defn)
            monstre.subir_degats(dmg_perso)
            print(f"{p.name} attaque ({dmg_perso} dmg) -> {monstre.pv} pv restants")

    if not monstre.est_vivant():
        print(f"{monstre.name} est vaincu !")
        narration_nouvelle_vague(monstre)
        return tour + 1

    cibles = [p for p in team if p.est_vivant()]
    if cibles:
        cible = random.choice(cibles)
        dmg = monstre.attaquer(cible)
        print(f"{monstre.name} attaque {cible.name} ({dmg} dmg) -> {cible.pv} pv restants")
        if not cible.est_vivant():
            print(f"{cible.name} est vaincu !")
    
    return tour + 1

def combat_test(team, monstre):
    print("=== DEBUT COMBAT ===")
    print(f"{team[0].name} VS {monstre.name}")
    print("--------------------")
    
    tour = 1
    while any(p.est_vivant() for p in team) and monstre.est_vivant():
        tour = combat_detail(tour, monstre, team)
    
    if not any(p.est_vivant() for p in team):
        print("La team a été vaincue !")

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