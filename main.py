from player import *
import time
from battle import *





def invallid():
    print('invallid input')
#rooms 

def hallway():
    searched:bool = False
    loosegold:int = 50
    global gold
    while True:
        print('what would you like to do \ exit , search , proceed')
        command = input('>')
        if command == "exit":
            break
        elif command == "search":
            if searched== False:
                searched=True
                print('you found 50GP')
                gold += 50
            else:
                print('there is nothing')   
        elif command == "proceed": 
            print('this area is part of the further dungeions expanction pack \ for £60 you can unlock more features and a pre order bonus of 100GP')        
        else:
            invallid()




#is_alive = True

pn = player.playername
alive= player.is_alive
gold:int=10
key=False

while alive ==True:
    
    print('many years ago there were 4 crystals ')
    print('greetings adventurer what is your name ')
    pn=input()
    
    if pn == 'leroy jenkins':
        print('"ok lets to this LEROYYYY JENKINS"')
        print('you ran in without planning or prepperation')
        time.sleep(1)
        print('"he just ran in"')
        time.sleep(1)
        print('"save him"')
        print('you are overwhelmed by dragons')
        print('and MISSIGNO')
        print('@@@@@')
        print('@@@@@')
        print('@@@@@')
        print('@@@@@')
        print('@@@@@')
        print('@@@@@@@@@@@')
        print('@@@@@@@@@@@')
        print('@@@@@@@@@@@')
        print('@@@@@@@@@@@')
        print('@@@@@@@@@@@')
        print('@@@@@@@@@@@')
        print('you died')
        alive = False
    else:
        print(f'welcome ',pn)
        print('what is your class')
        player_class = input()
        if player_class == "worrior":
            player.worrior(player)

        if player_class == "mage":
            player.mage(player)    
        print('you have chosen mage ')

    print('you awake in a large room')
    
    battle(slime)

    print('"phew that was close"')
    time.sleep(1)
    while True:
        print('there are two doors in front of you \ a door to the left and a door to the right ')
        print('type left or right to choose a room ')
        action = input(">")
        if action == "left":
            print('you go down the hallway')
            hallway()
        elif action =="right":
            if key == True:
                print('you leave the dungeon')
                print('you win')
                break
            else:
                print('the door is locked')   
        else:
            print('incorrect command')          
print('game over')


