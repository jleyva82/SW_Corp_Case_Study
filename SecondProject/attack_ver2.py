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