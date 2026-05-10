from random import choice

#monster/enemy
monsters = [
    ("Zephyr", 13, 30, 30),
    ("Pyro", 12, 29, 29),
    ("Terra", 11, 28, 28),
    ("Hydra", 10, 27,27),
]

dungeon_room = 1

print("Welcome to the dungeon game!")
#player 
name = input("What is your name? ").capitalize() 
permanent_playerhp = 0
player_hp = 0
player_atk = 0
level = 1
experience = 0
gold = 0 #nakakakuha ng gold every kill ng monster at level up

classes = ["Fighter", "Mage", "Assassin"] #fighter can block an attack, mage can heal, assassin can counter-attack
class_choice = input(f"\nChoose your class {name} {classes} : ").capitalize()

def spawn_monster(monsters_list):
    monster = choice(monsters_list)
    return monster

def level_up():
    global level, experience, gold
    level += 1
    experience = 0
    gold += 10
    print(f"\nYou leveled up! You are now level {level}.\n")

def gain_experience(amount):
    global experience
    experience += amount
    print(f"\nYou gained {amount} experience points!")
    if experience >= 100:
        level_up()

def attack():
    global monsthp
    monsthp -= player_atk
    print(f"\nYou attack the enemy! Dealt {player_atk} damage!")
    print(f"{monstname} HP is now {monsthp}.")
    gain_experience(20)

def block():
    print("\nYou defend against the attack!")
    gain_experience(10)

def heal():
    global player_hp
    if player_hp < 80:
        player_hp += 13
        if player_hp >= 80:
            player_hp = 80
        print(f"Player HP: {player_hp}")
    else:
        print("HP is already full!")
    gain_experience(10)

def counter_attack(): #nagtake ng damage yung player pero mas mababa sa original damage ng monster since nag counter attack player
    counterdamge = 6
    global monsthp, monstatk
    monstatk -= 2
    monsthp -= counterdamge
    print(f"\nYou've countered an attack and dealt {counterdamge} damage! ")
    print(f"{monstname} HP is now {monsthp}.")
    gain_experience(10)

def display_stats():
    print("\nPLAYER STATS:")
    print(f"Name: {name}")
    print(f"Class: {class_choice}")
    print(f"HP: {permanent_playerhp}")
    print(f"Attack: {player_atk}")
    print(f"Gold: {gold}")
    print(f"Level: {level}")
    print(f"Experience: {experience}")

def current_stats():
    print("\nPLAYER STATS:")
    print(f"Name: {name}")
    print(f"Class: {class_choice}")
    print(f"HP: {player_hp}")
    print(f"Attack: {player_atk}")
    print(f"Gold: {gold}")
    print(f"Level: {level}")
    print(f"Experience: {experience}")

def display_mainmenu():
    mainmenu = ["1: Enter Dungeon", "2: View Stats", "3: Exit"]
    print("\nChoose what to do")
    for menu_item in mainmenu:
        print(menu_item)

def monster_attack():
    global player_hp
    player_hp -= monstatk
    print(f"\nThe monster dealt {monstatk} damage to you!\n")  
    print(f"HP: {player_hp}\n")

def player_attack():
    global class_choice
    if class_choice == "Fighter" or class_choice == "fighter":
        fighter_attack = input("\nChoose an action (attack, block, retreat): \n> ")
        if fighter_attack == "attack":
            attack()             
        
        elif fighter_attack == "block":
            block()
        
        elif fighter_attack == "retreat":
            print("You run away! Returning to main menu.")

        else:
            print("Invalid action, try again.")

    elif class_choice == "Mage" or class_choice == "mage":
        mage_attack = input("\nChoose an action (attack, heal, retreat): \n> ")
        if mage_attack == "attack":
            attack()             
            
        elif mage_attack == "heal":
            heal()
            
        elif mage_attack == "retreat":
            print("You run away! Returning to main menu.")

        else:
            print("Invalid action, try again.")

    elif class_choice == "Assassin" or class_choice == "assassin": 
        assassin_attack = input("\nChoose an action (attack, counter, retreat): \n> ")
        if assassin_attack == "attack":
            attack()             
            
        elif assassin_attack == "counter":
            counter_attack()
            
        elif assassin_attack == "retreat":
            print("You run away! Returning to main menu.")

        else:
            print("Invalid action, try again.")
            
while True:
    if class_choice == "Fighter" or class_choice == "fighter":
        print("You have selected fighter class! ")
        permanent_playerhp = 100
        player_hp = 100
        player_atk = 10
        break
    elif class_choice == "Mage" or class_choice == "mage":
        print("You have selected mage class! ")
        permanent_playerhp = 80
        player_hp = 80
        player_atk = 8
        break
    elif class_choice == "Assassin" or class_choice == "assassin":
        print("You have selected assassin class! ")
        permanent_playerhp = 90
        player_hp = 90
        player_atk = 9
        break
    else:
        print("Invalid Class Choice!")
        class_choice = input(f"Choose your class {name} {classes} : ").capitalize()  
        
while True:
    display_mainmenu()
    action = input("> ")

    if action == "1":
        print(f"\nYou entered a dungeon. Room {dungeon_room}")
        monstname, monstatk, monsthp, monster_hp = spawn_monster(monsters)
        print(f"You have encountered a {monstname} wtih {monsthp} HP! ")

        while True:
            if class_choice == "Fighter" or class_choice == "fighter":
                fighter_attack = input("\nChoose an action (attack, block, retreat): \n> ")
                if fighter_attack == "attack":
                    attack()             
                
                elif fighter_attack == "block":
                    block()
                
                elif fighter_attack == "retreat":
                    print("You run away! Returning to main menu.")
                    break
                else:
                    print("Invalid action, try again.")
                    continue

            elif class_choice == "Mage" or class_choice == "mage":
                mage_attack = input("\nChoose an action (attack, heal, retreat): \n> ")
                if mage_attack == "attack":
                    attack()             
                    
                elif mage_attack == "heal":
                    heal()
                    
                elif mage_attack == "retreat":
                    print("You run away! Returning to main menu.")
                    break
                else:
                    print("Invalid action, try again.")
                    continue

            elif class_choice == "Assassin" or class_choice == "assassin": 
                assassin_attack = input("\nChoose an action (attack, counter, retreat): \n> ")
                if assassin_attack == "attack":
                    attack()             
                    
                elif assassin_attack == "counter":
                    counter_attack()
                    
                elif assassin_attack == "retreat":
                    print("You run away! Returning to main menu.")
                    break
                else:
                    print("Invalid action, try again.")
                    continue
            if monsthp > 0:
                monster_attack()
            else:
                gold += 10
                print(f"\nYou defeated the {monstname}")
                print(f"\nYou gain 10 golds for defeating the monster!\n")
                monsthp = monster_hp
                dungeon_room += 1
                if dungeon_room <= 3:
                    print(f"\nYou are in room {dungeon_room} of the dungeon! ")
                    monstname, monstatk, monsthp, monster_hp = spawn_monster(monsters)
                    print(f"New {monstname} with {monsthp} appeared! ")
                    continue
                else:
                    dungeon_room = 1
                    print("\nYou cleared the dungeon! Returning to main menu")
                    break
            if player_hp > 0:
                continue
            else:
                print("You died! Returning to main menu")
                player_hp = permanent_playerhp
                break

    elif action == "2":
        display_stats()
        continue

    elif action == "3":
        print(f"Exiting... bye {name}!")
        break

    else: 
        print("Invalid Choice! Enter number between 1 to 3!")
        continue
