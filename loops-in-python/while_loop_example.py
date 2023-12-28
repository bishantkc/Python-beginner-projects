import random

player_hp = 300
enemy_dmg_low = 60
enemy_dmg_high = 80

while player_hp > 0:
    dmg = random.randrange(enemy_dmg_low,enemy_dmg_high)
    player_hp = player_hp - dmg

    if player_hp <= 30:
        player_hp = 30

    print("Enemy strikes for ", dmg, "points of damage. Current hp is",player_hp )

    if player_hp > 30:  #continue will not let loop end and start again
        continue        #another way: hp == 30 and print (same thing will happen

    print("You have low health. You have been teleported.")
    break