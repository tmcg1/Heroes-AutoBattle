def attack(enemy, dmg):
    if enemy.hp > 0:
        enemy.hp = enemy.hp - dmg
        if enemy.hp <= 0:
            enemy.hp = 0
            enemy.alive = False
