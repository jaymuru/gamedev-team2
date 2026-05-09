from random import choice

#monster/enemy
monsters = [
    ("Zephyr", 13, 30),
    ("Pyro", 12, 29),
    ("Terra", 11, 28),
    ("Hydra", 10, 27),
]

room_dungeon = 0

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

    if monsthp > 0:
        monster_attack()
        print(f"\nThe monster dealt {monstatk} damage to you!")  
        print(f"Player HP: {player_hp}\n")

def block():
    print("\nYou defend against the attack!")
    gain_experience(10)

def heal():
    global player_hp
    if player_hp < 65:
        player_hp += 8
        if player_hp >= 65:
            player_hp = 65
        print(f"Player HP: {player_hp}")
    else:
        print("HP is already full!")
    gain_experience(10)

    if monsthp > 0:
        monster_attack()

def counter_attack(): #nagtake ng damage yung player pero mas mababa sa original damage ng monster since nag counter attack player
    counterdamge = 6
    global monsthp, monstatk
    monstatk -= 2
    monsthp -= counterdamge
    print(f"\nYou've countered an attack and dealt {counterdamge} damage! ")
    print(f"{monstname} HP is now {monsthp}.")
    if monsthp > 0:
        monster_attack()
        print(f"\nThe monster dealt {monstatk} damage to you!")  
        print(f"Player HP: {player_hp}\n")
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

def display_menu2():
    menu2 = ["1: Continue fighting", "2: View Stats", "3: Return to main menu"]
    print("\nWhat do you want to do next?")
    for menu_item in menu2:
        print(menu_item)

def monster_attack():
    global player_hp
    player_hp -= monstatk

def player_attack():
    global class_choice, monsthp, gold

    if class_choice == "Fighter" or class_choice == "fighter":
            fighter_attack = input("\nChoose an action (attack, block, retreat): \n> ")
            if fighter_attack == "attack":
                attack()             
            
            elif fighter_attack == "block":
                block()
            
            elif fighter_attack == "retreat":
                print("You run away! Returning to main menu.")
                return True
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
            return True 
            
        else:
            print("Invalid action, try again.")

    elif class_choice == "Assassin" or class_choice == "assassin": #counter attack, you deal damage to monster kahit turn pa lang ng monster
        assassin_attack = input("\nChoose an action (attack, counter, retreat): \n> ")
        if assassin_attack == "attack":
            attack()             
            
        elif assassin_attack == "counter":
            counter_attack()
            
        elif assassin_attack == "retreat":
            print("You run away! Returning to main menu.")
            return True
        else:
            print("Invalid action, try again.")
    
    if monsthp <= 0:
        gold += 10
        print(f"\nYou defeated the {monstname}!\n")
        print(f"\nYou gain 10 golds for defeating the monster!\n")
        return True
    
    return False 

while True:
    if class_choice == "Fighter" or class_choice == "fighter":
        print("You have selected fighter class! ")
        permanent_playerhp = 75
        player_hp = 75
        player_atk = 10
        break
    elif class_choice == "Mage" or class_choice == "mage":
        print("You have selected mage class! ")
        permanent_playerhp = 65
        player_hp = 65
        player_atk = 6
        break
    elif class_choice == "Assassin" or class_choice == "assassin":
        print("You have selected assassin class! ")
        permanent_playerhp = 70
        player_hp = 70
        player_atk = 8
        break
    else:
        print("Invalid Class Choice!")
        class_choice = input(f"Choose your class {name} {classes} : ").capitalize()  
        
while True:
    display_mainmenu()
    action = input("> ")

    if action == "1":
        print("\nYou entered a dungeon.")
        monstname, monstatk, monsthp = spawn_monster(monsters)
        print(f"You have encountered a {monstname} wtih {monsthp} HP! ")

        while monsthp > 0:
            defeated = player_attack()
            if defeated:
                break
    
            if monsthp <= 0:
                spawn_monster(monsters)
        
    elif action == "2":
        display_stats()
        continue

    elif action == "3":
        print(f"Exiting... bye {name}!")
        break

    else: 
        print("Invalid Choice! Enter number between 1 to 3!")
        continue
    display_menu2()
    next_choice = input("> ")
    if next_choice == "1":
        continue # continue is used to skip the rest of the code in the loop and start the next iteration of the loop(continue fighting/the loop)
    elif next_choice == "2":
        current_stats() 
    elif next_choice == "3":
        player_hp = permanent_playerhp
        print("Returning to the main menu.\n")
    else:
        print("Invalid choice. Returning to main menu!\n")
