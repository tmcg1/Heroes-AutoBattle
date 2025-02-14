import pygame

def cooldown_ready(self, counter, cooldown):
    regeneration_cooldown = getattr(self, counter) - (pygame.time.get_ticks())
    if regeneration_cooldown <= 0:
        new_counter = getattr(self, counter) + getattr(self, cooldown)
        setattr(self, counter, new_counter)
        return True
    return False