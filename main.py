from db_init import personnages, monstres
from game import choix_personnage, combat_test
from utils import get_db, get_random_monster, scores_bdd, afficher_scores, sauvegarde_scores, menu_fin_partie
from models import Personnage, Monstre

def afficher_menu_choix():
    print("1) Démarrer le jeu")
    print("2) Afficher le classement")
    print("3) Quitter")

def choix_console():
    choix = input("Votre choix : ")
    while choix not in ["1", "2", "3"]:
        print("Choisis bien golmon")
        choix = input("Votre choix : ")
    return choix


if __name__ == "__main__":
    db = get_db()
    monstre_data = get_random_monster(db)
    while True : 
        afficher_menu_choix()
        choix = choix_console()

        if choix == "1" :   
            pseudo = input("Entrez votre pseudo : ")
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
                score = combat_test(team, monstre_test)
                sauvegarde_scores(pseudo, score)

                choix_fin = menu_fin_partie()
                if choix_fin == "1":
                    continue
                else:
                    print("C'est ciao !")
                    break

        elif choix == "2":
            afficher_scores()
        
        elif choix == "3":
            print("C'est ciao !")
            break