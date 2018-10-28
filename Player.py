class Player:

    def __init__(self):
        self.hit = 100
        self.atk = 9
        self.df = 11
        self.agl = 8
        self.int = 6
        self.lck = 4

    def setHit(self, dmg):
        self.hit = self.hit-dmg

    def getHit(self):
        return self.hit

    def getAtk(self):
        return self.atk

    def getDef(self):
        return self.df

    def getAgl(self):
        return self.agl

    def getInt(self):
        return self.int

    def getLck(self):
        return self.lck
