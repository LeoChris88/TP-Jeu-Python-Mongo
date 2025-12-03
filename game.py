# game.py (debut)
import array
from utils import get_db, get_random_monster, calcul_degats
from models import Personnage, Monstre
from db_init import personnages, monstres
import time

def choix_personnage(personnages):
    team = []
    while team.__len__() < 3:
        print("=== BIENVENUE DANS LE JEU PYTHON MONGO ===\n")
        time.sleep(1)
        print("=== COMPOSEZ VOTRE TEAM (3 personnages) ===")
        time.sleep(1)
        print("Liste des personnages disponibles :\n")
        time.sleep(1)
        list = [{"Guerrier"}, {"Mage"}, {"Archer"}, {"Voleur"}, {"Paladin"}, {"Sorcier"}, {"Chevalier"}, {"Moine"}, {"Berserker"}, {"Chasseur"}]
        print(list)
        break

    choice = input("tapez entre 1 et 10 pour choisir votre personnage : ")
    if choice == "1":
        p1 = Personnage("Guerrier", 15, 10, 100)
        team.append(p1)
    elif choice == "2":
        p2 = Personnage("Mage", 20, 5, 80)
        team.append(p2)
    elif choice == "3":
        p3 = Personnage("Archer", 18, 7, 90)
        team.append(p3)
    elif choice == "4":
        p4 = Personnage("Voleur", 22, 8, 85)
        team.append(p4)
    elif choice == "5":
        p5 = Personnage("Paladin", 14, 12, 110)
        team.append(p5)
    elif choice == "6":
        p6 = Personnage("Sorcier", 25, 3, 70)
        team.append(p6)
    elif choice == "7":
        p7 = Personnage("Chevalier", 17, 15, 120)
        team.append(p7)
    elif choice == "8":
        p8 = Personnage("Moine", 19, 9, 95)
        team.append(p8)
    elif choice == "9":
        p9 = Personnage("Berserker", 23, 6, 105)
        team.append(p9)
    elif choice == "10":
        p10 = Personnage("Chasseur", 16, 11, 100)
        team.append(p10)
    else:
        print("Choix invalide, veuillez réessayer.")
        return choix_personnage(personnages)
    print("\n=== TEAM VALIDÉE ===")
    for p in team:
        print(f"- {p.name}")

    return team

# def combat_test(perso, monstre):
#     print("=== DEBUT COMBAT ===")
#     print(f"{personnages.name} VS {monstres.name}")
#     print("--------------------")

#     tour = 1

#     while personnages.est_vivant() and monstres.est_vivant():
#         print(f"\n--- TOUR {tour} ---")

#         dmg_perso = calcul_degats(personnages.atk, monstres.defn)
#         monstres.subir_degats(dmg_perso)
#         print(f"{personnages.name} attaque ({dmg_perso} dmg) -> {monstres.pv} pv reste")

#         if not monstres.est_vivant():
#             print(f"\n>> Le monstre {monstres.name} est vaincu !")
#             break

#         dmg_monstre = monstres.attaquer(perso)
#         print(f"{monstres.name} riposte ({dmg_monstre} dmg) -> {personnages.pv} pv reste")

#         tour += 1

#     print("\n=== FIN DU COMBAT ===\n")


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

        print("Monstre tiré pour le combat :", monstre_test.name)

        # combat_test(choix_personnage, monstre_test)