import pygame

class HealthBar:
    def __init__(self, x, y, w, h, hp, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
