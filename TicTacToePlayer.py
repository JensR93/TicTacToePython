class TicTacToePlayer():
    def __init__(self,name,char):  
        self.name = name;  
        self.char = char;  
        self.siege=0
        self.niederlage=0
        self.unentschieden=0

    def displayFullStats(self):
        print("Name: %s\nZeichen: %s \nsiege: %s \niederlage: %s \nunentschieden: %s"%(self.name,self.char,self.siege,self.niederlage,self.unentschieden))  

    def display (self):  
        print("Name: %s\nZeichen: %s"%(self.name,self.char))  