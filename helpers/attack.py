def attack(self, enemy, dmg):
    if hasattr(self, 'evolution') and self.evolution:
        self.max_hp += 1

    if enemy.hp > 0:
        enemy.hp = enemy.hp - dmg
        if enemy.hp <= 0:
            enemy.hp = 0
            enemy.alive = False
