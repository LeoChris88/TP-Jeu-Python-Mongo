class Personnage:
    def __init__(self, name, atk, defn, pv_max):
        self.name = name
        self.atk = atk
        self.defn = defn
        self.pv_max = pv_max
        self.pv = pv_max

    def reset(self):
        self.pv = self.pv_max

    def est_vivant(self):
        return self.pv > 0
    
    def subir_degats(self, montant):
        self.pv -= montant
        if self.pv < 0:
            self.pv = 0

    def attaquer(self, cible):
        from utils import calcul_degats
        dmg = calcul_degats(self.atk, cible.defn)
        cible.subir_degats(dmg)
        return dmg


class Monstre:
    def __init__(self, name, atk, defn, pv_max):
        self.name = name
        self.atk = atk
        self.defn = defn
        self.pv_max = pv_max
        self.pv = pv_max

    def reset(self):
        self.pv = self.pv_max

    def est_vivant(self):
        return self.pv > 0
    
    def subir_degats(self, montant):
        self.pv -= montant
        if self.pv < 0:
            self.pv = 0

    def attaquer(self, cible):
        from utils import calcul_degats
        dmg = calcul_degats(self.atk, cible.defn)
        cible.subir_degats(dmg)
        return dmg
    
def convert_to_monster(monstre_dict):
    return Monstre(monstre_dict['name'], monstre_dict['atk'], monstre_dict['defn'], monstre_dict['pv'])