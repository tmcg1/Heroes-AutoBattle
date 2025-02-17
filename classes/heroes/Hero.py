class Hero:
    def __init__(self, hp):
        self.alive = True
        self.max_hp = hp
        self.current_dmg = ""
        self.current_heal = ""
        self.level = 1
        self.exp = 0