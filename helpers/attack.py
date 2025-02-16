from helpers.draw import draw_text


def attack(enemy, dmg):
    if enemy.hp > 0:
        enemy.hp = enemy.hp - dmg
        enemy.current_dmg = "-" + str(dmg)

        if enemy.hp <= 0:
            enemy.hp = 0
            enemy.alive = False
