class Character:
    def __init__(self, name, atk, defn, pv_max):
        self.name = name
        self.atk = atk
        self.defn = defn
        self.pv_max = pv_max
        self.pv = pv_max

    def reset(self):
        self.pv = self.pv_max


class Monster:
    def __init__(self, name, atk, defn, pv_max):
        self.name = name
        self.atk = atk
        self.defn = defn
        self.pv_max = pv_max
        self.pv = pv_max

    def reset(self):
        self.pv = self.pv_max