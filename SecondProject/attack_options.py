from classes.enemy import Enemy         #imports the class 'Enemy' from the file 'enemy.py' in the directory 'classes'
                                        #because we imported the class 'Enemy' it can do be called out in this script

enemy = Enemy(200,60)                   #creates an object from the class of Enemy with 200hp and 60mp
print(enemy.get_hp())                   #prints out the hp
print(enemy.get_mp())                   #prints out the mp

'''
option 2
class Enemy:   #a class is a blueprint
    hp = 200   #now all enemys have 200hp

    def __init__(self, atklow, atkhigh):   #creates init function to input low and high attacks
        self.atklow = atklow
        self.atkhigh = atkhigh


    def getAtk(self):                    #function within a class will put 'self' as its parameter
        print("atk is", self.atklow)

    def getHP(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 49)                        #asign 'enemy1' as type of the class Enemy
enemy1.getAtk()                               #calls out the getAtk function
enemy1.getHP()                                #call out the getHP function

enemy2 = Enemy(75, 90)                        #repeat for 'enemy2'
enemy2.getAtk()
enemy2.getHP()
'''

'''
option 3
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


#This is a simple attack script for an rpg like game
#it uses the random from range function from the random library
#important to use break of while loop as there is a value safegard that creates a continuous loop

#could be optimized to include 'super effective' or 'not very effective' damage types
'''