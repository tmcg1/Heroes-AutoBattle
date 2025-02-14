def heal(self, healing_points):
    if self.hp < self.max_hp and self.alive:
        self.hp += healing_points

        if self.hp > self.max_hp:
            self.hp = self.max_hp