class Enemy:                            #creates the 'Enemy' class
    def __init__(self, hp, mp):         #defines what is in each object within the class
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    def get_hp(self):                   #function to return hp
        return self.hp

    def get_mp(self):                   #function to return mp
        return self.mp
