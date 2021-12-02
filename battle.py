from player import player


#----------Spells-----------
class dmgspell:
    def __init__(self,name,dmg,mpcost) -> None:
        self.name=name
        self.dmg=dmg
        self.mpcost=mpcost

fire =dmgspell("fire",5,2)


class healspell:
    def __init__(self,name,heal,mpcost):
        self.name=name
        self.heal=heal
        self.mpcost=mpcost
 
   
cure =healspell("cure",5,2)    



#---------bad guys ----------

class Enemy:
    def __init__(enemy,name,attack,maxhp,currhp,mp, speed):
        enemy.name=name
        enemy.attack=attack
        enemy.maxhp=maxhp
        enemy.currhp=currhp
        enemy.maxmp=mp
        enemy.speed=speed

bat = Enemy("bat",1,10,10,0,10)
slime =Enemy("slime",1,20,20,0,3)

global isalive


def player_move():
    
    pass
def enemy_move():
    pass



def castheal(healspell):
        print(f'you cast {healspell.name} ')
        if (player.currhp + healspell.heal) > player.maxhp:
             player.currhp += healspell.heal
        elif player.currhp + healspell < player.maxhp:
             currhp= player.maxhp
        else:
            print('your at max hp')     

def attack():
    
    print(f'you attack ') 
    Enemy.currhp -= player.attack
    print(f'you hit {Enemy.name} for {player.attack} Damage')


def battle(Enemy):
    
    while Enemy.currhp >= 0:
    
        print(Enemy.name +' is in your way')
        print(f'your hp is {player.currhp}' )

        #Speed check to decide who goes first 
        if player.speed > Enemy.speed:
            print('your move \n what would you like to do -magic -attack')
            command = input('>')
            if command == "attack" or "a":
               attack()
            elif command == "magic" or "m":
                castheal(cure)
            print(f"{Enemy.name}'s turn")
            player.currhp -=Enemy.attack
            print(f'{Enemy.name} hit you for {Enemy.attack}')
            if player.currhp <= 0:
                print('you are dead')
                player.is_alive = False
        if player.speed < Enemy.speed:
            player.currhp -= Enemy.attack
            print(f'{Enemy.name} hit you for for {Enemy.attack} Damage')
            print(player.currhp) 
            if player.currhp <= 0:
                print('you are dead')
                alive = False
            print('your move \n what would you like to do -magic -attack')
            command:str = input('>')
            if command == "attack" or "a":
                attack() 
            elif command == "magic" or "m":
                castheal(cure)
            else:
                print('invalid command')    
    print('you win')               
    






     