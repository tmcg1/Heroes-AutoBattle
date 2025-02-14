from helpers.attack import attack
from helpers.cooldown_ready import cooldown_ready
import random

class Druid:
    def __init__(self):
        self.hp = 60
        self.max_hp = self.hp
        self.alive = True
        self.swipe_cooldown = 2000
        self.swipe_counter = self.swipe_cooldown
        self.bloodlust = False
        self.evolution = False
        self.bloodlust_counter = 1

    def swipe(self, enemy):
        if cooldown_ready(self, "swipe_counter", "swipe_cooldown"):
            dmg = random.randint(1, 3)

            if self.bloodlust:
                dmg += self.bloodlust_counter
                self.bloodlust_counter += 1

            attack(self, enemy, dmg)

    def add_bloodlust(self):
        self.bloodlust = True

    def add_evolution(self):
        self.evolution = True
