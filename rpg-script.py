import random

#player choice of class

class rogue:
    hpmax = 50
    hpmin = 10
    atkl = 15
    atkh = 30

class wizard:
    hpmax = 60
    hpmin = 10
    atkl = 20
    atkh = 40

class warrior:
    hpmax = 75
    hpmin = 10
    atkl = 30
    atkh = 60

class bard:
    hpmax = 40
    hpmin = 10
    atkl = 10
    atkh = 20

    
#Enemies:  Is there a such thing as a subclass?
    
class beast:
    hpmax = 45
    hpmin = 0
    atkl = 5
    atkh = 15

class bandit:
    hpmax = 30
    hpmin = 0
    atkl = 10
    atkh = 20

class soldier:
    hpmax = 60
    hpmin = 0
    atkl = 20
    atkh = 40

class boss:
    hpmax = 100
    hpmin = 0
    atkl = 20
    atkh = 35

    

player = input("Please select a class(rogue, wizard, warrior, or bard):")
#Figure out how to reference the classes set out above.

if player == rogue:
    player = class rogue
elif player == wizard:
    player == class wizard
elif player == warrior:
    player == class warrior
elif player == bard:
    player == class bard
else:
    print("Please select a proper class" + player)

enemy =
'''How to randomy pick an enemy...may need a different module for enemies only
and another for hero classes'''

playerhp = input.hpmax

while playerhp > 0:
    dmg = random.randrange()
    playerhp = playerhp - dmg

if playerhp <=10:
    playerhp = 10
print("You are going to die, transport to your camp for healing")
