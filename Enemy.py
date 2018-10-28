class Enemy:

    def __init__(self):
        self.hit = 80
        self.atk = 5
        self.df = 8
        self.agl = 4
        self.int = 2
        self.lck = 1

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
