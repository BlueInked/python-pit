from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 120, "black")
blizzard = Spell("Blizzard", 11, 90, "black")
quake = Spell("Quake", 13, 125, "black")
cosmic = Spell("Cosmic", 20, 200, "black")
doom = Spell("Doom",30, 300, "black")

#White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 20, 220, "white")


#Healing Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
superelixir = Item("Super Elixir", "elixir", "Fully restores party's HP/MP", 9999)

#Damage Items
bomb = Item("Bomb", "attack", "Deals 500 damage", 500)
rock = Item("Rock", "attack", "Deals 5 damage", 5)

player_spells = [fire, thunder, blizzard, cosmic, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, superelixir, bomb, rock]

#Instantiate People
player = Person(460, 65, 60, 34, player_spells , player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("============================")
    player.choose_action()
    choice = input("Choose actions: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index ==1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

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
            print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("--------------------------------------------------")
    print("Enemy HP:",  bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You have Defeated the enemy!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your HP is zero, you  have been defeated!" + bcolors.ENDC)
        running = False
