import random

from classes.heroes.Hero import Hero
from helpers.attack import attack
from helpers.cooldown_ready import cooldown_ready
from helpers.heal import heal

class Paladin(Hero):
    def __init__(self):
        self.hp = 50
        self.holy_strike_cooldown = 2500
        self.holy_strike_counter = self.holy_strike_cooldown
        self.holy_light_cooldown = 5000
        self.holy_light_counter = self.holy_light_cooldown
        self.growing_light = False
        self.growing_light_counter = 1
        super().__init__(self.hp)

    def holy_strike(self, enemy):
        if cooldown_ready(self, "holy_strike_counter", "holy_strike_cooldown"):
            attack(self, enemy, random.randint(3, 5))

    def holy_light(self):
        if cooldown_ready(self, "holy_light_counter", "holy_light_cooldown"):
            healing_points = random.randint(10, 15)

            if self.growing_light:
                healing_points += self.growing_light_counter
                self.growing_light_counter += 1

            heal(self, healing_points)

    def add_growing_light(self):
        self.growing_light = True
