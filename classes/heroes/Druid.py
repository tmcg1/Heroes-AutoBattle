from helpers.cooldown_ready import cooldown_ready
import random

class Druid:
    def __init__(self):
        self.hp = 60
        self.max_hp = self.hp
        self.alive = True
        self.swipe_cooldown = 1800
        self.swipe_counter = self.swipe_cooldown

    def swipe(self, enemy):
        if cooldown_ready(self, "swipe_counter", "swipe_cooldown"):
            if enemy.hp > 0:
                attack_dmg = random.randint(1, 3)
                enemy.hp = enemy.hp - attack_dmg
                if enemy.hp <= 0:
                    enemy.hp = 0
                    self.alive = False