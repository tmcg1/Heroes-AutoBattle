from classes.heroes.Hero import Hero
from helpers.attack import attack
from helpers.cooldown_ready import cooldown_ready
import random

class Druid(Hero):
    def __init__(self):
        self.hp = 60
        self.swipe_cooldown = 2000
        self.swipe_counter = self.swipe_cooldown
        self.bloodlust = False
        self.evolution = False
        self.bloodlust_counter = 1
        super().__init__(self.hp)

    def druid_attack(self, enemy, dmg):
        if self.evolution:
            self.max_hp += 1

        attack(enemy, dmg)

    def swipe(self, enemy):
        if cooldown_ready(self, "swipe_counter", "swipe_cooldown"):
            dmg = random.randint(1, 3)

            if self.bloodlust:
                dmg += self.bloodlust_counter
                self.bloodlust_counter += 1

            self.druid_attack(enemy, dmg)

    def add_bloodlust(self):
        self.bloodlust = True

    def add_evolution(self):
        self.evolution = True
