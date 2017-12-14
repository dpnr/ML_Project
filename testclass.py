class test:
    firstvar = []
    def __init__(self,firstvar,secondvar):
        self.firstvar = firstvar
        self.secondvar = secondvar
    
    def setfirst(self,first):
        self.firstvar = first

    def getfistvar(self):
        return self.firstvar