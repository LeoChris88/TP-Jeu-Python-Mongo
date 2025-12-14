import array
import random
from utils import get_db, get_random_monster, calcul_degats, pause_rapide, pause_normal, narration_debut_combat, narration_nouvelle_vague, message_defaite
from models import Personnage, Monstre,  convert_to_monster
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
    print(liste)
    
    while len(team) < 3:
        choice = get_valid_int(f"Choisissez un personnage en tapant un nombre entre 1 et {len(liste)} :", len(liste))
        perso = personnages.pop(choice - 1)
        team.append(perso)
    
    afficher_team(team)
    print("\n=== TEAM VALIDÉE ===")
    return team 

def monstre_aleatoire(monstres): 
    return random.choice(monstres)

def combat_detail(tour, monstre, team):
    pause_rapide()
    print(f"\n--- TOUR {tour} ---")

    for p in team:
        if p.est_vivant():
            dmg_perso = max(0, p.atk - monstre.defn)
            monstre.subir_degats(dmg_perso)
            print(f"{p.name} attaque ({dmg_perso} dmg) -> {monstre.pv} pv restants")

    if not monstre.est_vivant():
        print(f"{monstre.name} est vaincu !")
        return "monstre_mort"

    cibles = []
    for p in team:
        if p.est_vivant():
            cibles.append(p)

    if len(cibles) > 0:
        cible = random.choice(cibles)
        dmg = monstre.attaquer(cible)
        print(f"{monstre.name} attaque {cible.name} ({dmg} dmg) -> {cible.pv} pv restants")

        if not cible.est_vivant():
            print(f"{cible.name} est vaincu !")

    return tour + 1

def team_vivant(team):
    return any(p.est_vivant() for p in team)

def combat_test(team, monstre):
    narration_debut_combat(team)    
    tour = 1
    vague = 1
    print(f"\n=== VAGUE {vague} ===")

    while True:
        if not team_vivant(team):
            message_defaite(vague)
            return vague
        resultat = combat_detail(tour, monstre, team)

        if resultat == "monstre_mort":
            vague += 1
            print(f"\nVAGUE {vague} !!!")
            narration_nouvelle_vague(monstre)
            for p in team:
                p.reset()
            nouveau = monstre_aleatoire(monstres)
            monstre = convert_to_monster(nouveau)
            print(f"\nNOUVEAU MONSTRE : {monstre.name} ({monstre.atk} atk, {monstre.defn} def, {monstre.pv} pv)")
            tour = 1
            continue
        tour = resultat