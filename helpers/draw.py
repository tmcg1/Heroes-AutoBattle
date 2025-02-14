import pygame

from constants.constants import WIN

druid_img = pygame.image.load(("./assets/bear.png"))
paladin_img = pygame.image.load(("./assets/paladin.png"))

def draw_images():
    WIN.blit(druid_img, (600, 430))
    WIN.blit(paladin_img, (680, 50))
    pygame.display.update()

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    WIN.blit(img, (x, y))
