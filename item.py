class item:

    def __init__(self, data):

        self.name   = data[0]
        self.hit    = data[1]
        self.atk    = data[2]
        self.df     = data[3]
        self.agl    = data[4]
        self.int    = data[5]
        self.lck    = data[6]
        self.InInv  = data[7]

    def getName(self):
        return self.name
