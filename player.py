class player:

    

    playername:str = 'bob'
    is_alive:bool = True
    def __init__(self,job,attack,maxhp,mp,speed,is_alive):
        self.job='no job'
        self.attack=0
        self.maxhp=0
        self.currhp=maxhp
        self.mp=0
        self.speed=0
        self.is_alive=True
        

    def worrior(self):
        self.job= 'fighter'
        self.attack=10
        self.maxhp=100
        self.maxmp=0
        self.speed =5

    def mage(self):
        self.job= 'mage'
        self.attack=20
        self.maxhp=50
        self.currhp=self.maxhp
        self.maxmp=10 
        self.speed=8   


