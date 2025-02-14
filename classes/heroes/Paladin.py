from helpers.cooldown_ready import cooldown_ready
import random

class Paladin:
    def __init__(self):
        self.hp = 50
        self.max_hp = self.hp
        self.alive = True
        self.holy_strike_cooldown = 2500
        self.holy_strike_counter = self.holy_strike_cooldown

    def holy_strike(self, enemy):
        if cooldown_ready(self, "holy_strike_counter", "holy_strike_cooldown"):
            if enemy.hp > 0:
                attack_dmg = random.randint(2, 5)
                enemy.hp = enemy.hp - attack_dmg
                if enemy.hp <= 0:
                    enemy.hp = 0
                    self.alive = False