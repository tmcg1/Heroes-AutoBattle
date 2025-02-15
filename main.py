import pygame

from classes.heroes.Druid import Druid
from classes.heroes.Paladin import Paladin
from classes.visuals.HealthBar import HealthBar
from constants.constants import WIN
from helpers.draw import draw_images, draw_text

pygame.font.init()

pygame.display.set_caption("Heroes AutoBattle")

clock = pygame.time.Clock()

druid = Druid()
paladin = Paladin()

# Druid effects
druid.add_bloodlust()
druid.add_evolution()

# Paladin effects
paladin.add_growing_light()

is_paused = True
run = True

while run:
    WIN.fill("teal")
    clock.tick(60)

    while druid.alive == False or paladin.alive == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

    druid.swipe(paladin)
    paladin.holy_strike(druid)
    paladin.holy_light()

    druid_health_bar = HealthBar(610, 760, 300, 40, druid.hp, druid.max_hp)
    paladin_health_bar = HealthBar(600, 0, 300, 40, paladin.hp, paladin.max_hp)

    druid_health_bar.draw(WIN)
    paladin_health_bar.draw(WIN)

    draw_text(f"{druid.hp} | {druid.max_hp}", 725, 765)
    draw_text(f"{paladin.hp} | {paladin.max_hp}", 725, 3)

    # GAME IS PAUSED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_images()

    pygame.display.update()

pygame.quit()

