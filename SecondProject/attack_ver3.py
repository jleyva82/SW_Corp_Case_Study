import random                           #necessary to import random function


playerhp = 260                           #sets player's base Health Points
enemyatklow = 60                         #sets enemy attack range(low)
enemyatkhigh = 80                                                #(high)

while playerhp > 0:                      #while the player has HP the enemy will attack
    dmg = random.randrange(enemyatklow, enemyatkhigh)      #uses "random.radrange(low,high)" to determine enemy's attack damage
    playerhp = playerhp - dmg            #calculate remainding HP

    if playerhp <= 30:                   #safegard for player
        playerhp = 30                    #reset of value to predetermined safegard value

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp) #careful, make sure this statement is nested in proper indentation
                                                                                 #it needs to be alinged outside the if statement
    if playerhp > 30:
        continue

    print("You have low health. You've been teleported to the nearest medical center.") #once safegard has been trigered communicate what has happened
    break                                                                               #and break the while loop