def heal(self, healing_points):
    if self.hp < self.max_hp and self.alive:
        self.hp += healing_points
        self.current_heal = "+" + str(healing_points)

        if self.hp > self.max_hp:
            self.hp = self.max_hp