from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#Black Magic
fire = Spell("Fire", 25, 300, "black")
thunder = Spell("Thunder", 25, 320, "black")
blizzard = Spell("Blizzard", 20, 200, "black")
quake = Spell("Quake", 30, 325, "black")
cosmic = Spell("Cosmic", 40, 600, "black")
doom = Spell("Doom",50, 800, "black")

#White Magic
cure = Spell("Cure", 25, 520, "white")
cura = Spell("Cura", 40, 820, "white")
curaga = Spell("Curaga", 60, 3000, "white")


#Healing Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
superelixir = Item("Super Elixir", "elixir", "Fully restores party's HP/MP", 9999)

#Damage Items
bomb = Item("Bomb", "attack", "Deals 500 damage", 500)
rock = Item("Rock", "attack", "Deals 5 damage", 5)

player_spells = [fire, thunder, blizzard, cosmic, cure, cura]
enemy_spells = [blizzard, cosmic, curaga]
player_items = [{"item": potion, "quantity": 17}, {"item": hipotion, "quantity": 4},
                {"item": superpotion, "quantity": 2}, {"item": elixir, "quantity": 5},
                {"item": superelixir, "quantity": 3}, {"item": bomb, "quantity": 7}, {"item": rock, "quantity": 15}]

#Instantiate People
player1 = Person("Cicyla: ", 3565, 157, 300, 183, player_spells , player_items)
player2 = Person("Rosalba:", 4500, 100, 330, 300, player_spells , player_items)
player3 = Person("Tivmeda:", 3120, 188, 200, 250, player_spells , player_items)

enemy1 = Person("Minion", 2000, 135, 350, 150, enemy_spells, [])
enemy2 = Person("Devos ", 17000, 217, 505, 300, enemy_spells, [])
enemy3= Person("Minion", 2000, 135, 350, 150, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("============================")

    print("\n\n")

    print("NAME                     HP                                                   MP")

    for player in players:
         player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose actions: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("You attacked " + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]
        elif index ==1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\n Not enough MP \n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == "black":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace(" ", "") + "." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "Item Not Available" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -=1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Super Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to" + enemies[enemy].name + "." + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

#check if battle if over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1
#check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You have Defeated the enemies!" + bcolors.ENDC)
        running = False
#check if enemy won
    elif defeated_players == 2:
        print(bcolors.FAIL + "Your HP is zero, you  have been defeated!" + bcolors.ENDC)
        running = False

    print("\n")
#enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0,2)
    #attack
        if enemy_choice == 0:
            target = random.randrange(0,3)
            enemy_dmg = enemies[0].generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for ", enemy_dmg, " points of damage.")
    #use magic
        elif enemy_choice == 1:
           spell, magic_dmg = enemy.choose_enemy_spell()
           enemy.reduce_mp(spell.cost)

           if spell.type == "white":
               enemy.heal(magic_dmg)
               print(bcolors.OKBLUE + "\n" + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP" + bcolors.ENDC)
           elif spell.type == "black":

               target = random.randrange(0, 3)

               players[target].take_damage(magic_dmg)

               print(bcolors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg),
                     "points of damage to " + players[target].name.replace(" ", "") + "." + bcolors.ENDC)

               if players[target].get_hp() == 0:
                   print(players[target].name.replace(" ", "") + " has died.")
                   del players[player]

           print(enemy.name.replace(" ", "") + " chose ", spell, " damage is ", magic_dmg)
