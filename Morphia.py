import random
import sys
import time


# Characters or Roles
class Assassin:
    """Initialize assassin class"""
    def __init__(self, name):
        self.name = name
        self.hp = 120
        self.attack = 90


class Warrior:
    """Initialize warrior class"""
    def __init__(self, name):
        self.name = name
        self.hp = 130
        self.attack = 80


class Archer:
    """Initialize Archer class"""
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 75

# Enemy


class Trolls:
    """Initialize Trolls class"""
    def __init__(self):
        self.name = 'Trolls'
        self.hp = 70
        self.attack = random.randint(15, 30)


class Goblins:
    """Initialize Goblins class"""
    def __init__(self):
        self.name = 'Goblins'
        self.hp = 100
        self.attack = random.randint(20, 40)


class FieryFiend:
    """Initialize Fiery Fiend class"""
    def __init__(self):
        self.name = 'Fiery Fiend'
        self.hp = 150
        self.attack = random.randint(30, 50)


class Dragon:
    """Initialize Dragon class"""
    def __init__(self):
        self.name = 'Dragon'
        self.hp = 250
        self.attack = random.randint(40, 70)

# Item


class Potions:
    def __init__(self):
        self.name = 'Potions'
        self.hp = random.randint(20, 50)


# Weapon
class Weapon:
    def __init__(self):
        self.name = "Weapon"
        self.attack = 20
        self.hp = 40


class Status:

    @staticmethod
    def stats(charac):
        """Displaying the stats in beginning"""
        print('\nThis are your stats')
        print(f'Attack: {charac.attack} damage')
        print(f'Health: {charac.hp} hp')

    @staticmethod
    def playing_stats(charac):
        """Displaying the status when playing"""
        print(f'Attack:{charac.attack}\t\tHealth:{charac.hp}')

    @staticmethod
    def dead(charac):
        """Check if the user is dead"""
        charac.hp = 0
        Status.playing_stats(charac)
        print("\nYou're dead")
        play_again = input('\nDo you want to play again?(y/n): ').lower()
        # IF the user choose no the game will exit
        if play_again not in ['y', 'yes']:
            sys.exit()
        else:  # It will print a space to clear the window and call again the title screen function
            print("\n" * 20)
            titlescreen()


def play(charac, status):
    """Simulate the game"""
    # TO clear the screen
    print("\n" * 20)
    # Starting the game
    start = f"\nHello {charac.name} you are in front of Ouranos Cave. Your quest is to find the Morphia Jewel that the" \
            f" Dragon Stole"
    # To display simulate printing
    for letter in start:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    # Ask user to enter the cave
    start_game = input("\nEnter the cave?(y/n): ").lower()
    # Flag to start the game
    if start_game in ['y', 'yes']:
        game_on = True
    else:
        game_on = False

    # Loop of the game
    while game_on:
        display = "\nYou've entered the cave, you begin to walk and there are Two paths. " \
                  "Choose: Forward and Left"
        # Simulate slow printing
        for letter in display:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)
        choose_path = input("\n> ").lower()

        # If the choose_path if user is forward
        while choose_path != "left":
            # Classes that need in this gameplay
            potion = Potions()
            weapon = Weapon()
            fiery_fiend = FieryFiend()
            dragon = Dragon()

            # Display
            print("\n-----------------------------------------------------------------")
            status.playing_stats(charac)
            print("\n\n\tThere is a boulder covering the path what do you want to do?")
            print("\t\t\tBreak\t\t\tInspect")
            print("----------------------------------------------------------------")
            # Get user input
            choose_path = input("\n> ").lower()

            # If the choose_path is inspect
            if choose_path == "inspect":
                print(f"You found your first {weapon.name}!!!")
                charac.attack += weapon.attack
                charac.hp += weapon.hp
                destroy = input("Use it to break the boulder?(y/n): ").lower()

                # if the answer is yes
                if destroy in ['y', 'yes']:
                    print("\n-------------------------------------------------------------------------")
                    status.playing_stats(charac)
                    print("\n\nThe Boulder turned into pieces")
                    print("You continue to walk... There are two paths. Choose: \n\t\t\tLeft\t\t\tForward")
                    print("-------------------------------------------------------------------------")
                    choose_path = input("\n> ").lower()

                    # If the user choose forward again
                    if choose_path == "forward":
                        print("\n--------------------------------------------------------------------------")
                        status.playing_stats(charac)
                        print(f"\n\nThere are {fiery_fiend.name}.\nAttack: {fiery_fiend.attack}\nHealth: {fiery_fiend.hp}")
                        print("--------------------------------------------------------------------------")
                        choose_path = input("Fight or Run?: ").lower()

                        # if the user chooses to fight
                        if choose_path == "fight":
                            fighting = True
                            while fighting:
                                # Simulation of fighting
                                print("\n------------------------------------------------------")
                                status.playing_stats(charac)
                                print(f'\n\nYou attacked. It dealt {charac.attack} damage')
                                fiery_fiend.hp -= charac.attack

                                # Check if someone is dead
                                if fiery_fiend.hp <= 0:
                                    fighting = False
                                    print('Fiery Fiend is dead')

                                    # Another Path
                                    print("\nYou continue to walk and see a two paths. Choose:\nRight\t\t\tLeft")
                                    # Get User input
                                    choose_path = input("\n> ").lower()
                                    # If user chooses to go right
                                    if choose_path == "right":
                                        print("\nThere is another boulder blocking the path. Do you want to destroy it?:")
                                        destroy = input('\n> ').lower()
                                        # If user choose yes
                                        if destroy in ['y', 'yes']:
                                            print('\nThe boulder turned into pieces!')
                                            print("You found a potion!!")
                                            potion.hp += charac.hp

                                            for _ in range(4):
                                                print("....")
                                                time.sleep(1)
                                            # The dragon will appear
                                            print("\nYou saw a big cast Shadow")
                                            print("\nROOOOAAARR!")
                                            print("\nThe dragon has appeared, You have to defeat the Dragon to retrieve the Morphia jewels.")

                                            # Simulate fighting
                                            ask = input("Attack or Run?:\n> ").lower()
                                            # IF the user chooses to attack
                                            if ask == "attack":
                                                # Active flag
                                                fighting = True
                                                # Fighting loop
                                                while fighting:
                                                    print("------------------------------------------------------------------------------------------------------")
                                                    # Display the users stats
                                                    status.playing_stats(charac)
                                                    print(f"\nYou attacked and it dealt {charac.attack} damage ")
                                                    dragon.hp -= charac.attack

                                                    # Check if the health of dragon is equal to zero and display the user has won
                                                    if dragon.hp <= 0:
                                                        print("\nYou defeated the Dragon!!! You won! The villagers are happy because the Morphia Jewels are back.")
                                                        play_again = input("\nDo you want to play again?(y/n): ").lower()

                                                        # Ask user if they want to play again
                                                        if play_again not in ['y', 'yes']:
                                                            sys.exit()
                                                        else:
                                                            titlescreen()
                                                    # IF the dragon is still alive
                                                    else:
                                                        # Display the stats of dragon
                                                        print("\nt")
                                                        status.playing_stats(dragon)
                                                        print(f"\n\nThe Dragon attacked and it dealt {dragon.attack} damage!")
                                                        charac.hp -= dragon.attack

                                                        # CHeck if the user is dead
                                                        if charac.hp <= 0:
                                                            fighting = False
                                                            status.dead(charac)
                                            # If the user chooses to run
                                            elif choose_path == "run":
                                                print("\nThe dragon blocked your way and attacked you")
                                                print("You pass out and became feast of the Dragon")
                                                status.dead(charac)
                                            # If the choose_path is invalid
                                            else:
                                                invalid = input('Do you want to quit?(y/n): ').lower()
                                                if invalid in ['y', 'yes']:
                                                    sys.exit()
                                                else:
                                                    print('Please enter a valid command')

                                    # if the user chooses to go left
                                    elif choose_path == "left":
                                        print("\nYou saw a spring")
                                        ask = input("\nDo you want to drink?(y/n): ").lower()

                                        # Ask the user he wants to drink
                                        if ask not in ['y', 'yes']:  # if the user chooses to not drink
                                            print("\nThe path going back was blocked")
                                            print("You can't destroyed it!")
                                            status.dead(charac)
                                        # IF the user drinks
                                        else:
                                            print("\nYou feel refreshed")
                                            for _ in range(4):
                                                print('.....')
                                                time.sleep(0.5)

                                            print("\nYou fall asleep and Died")
                                            status.dead(charac)
                                # If the fiery fiend is still alive
                                else:
                                    # Display the stats of fiery fiend
                                    print("\n")  # Adding spaces
                                    status.playing_stats(fiery_fiend)
                                    print(f'\n\nFiery fiend attacked. It dealt {fiery_fiend.attack} damage')
                                    charac.hp -= fiery_fiend.attack

                                    # Check if users hp is zero
                                    if charac.hp <= 0:
                                        fighting = False
                                        status.dead(charac)

                        # IF the user chooses to run
                        elif choose_path == 'run':
                            print('\nFiery Fiend heard you... Fiery Fiend chase you and caught you...')
                            print('You become their feast.\nYOU DIED!')
                            status.dead(charac)

                        # If user prompt an invalid answer
                        else:
                            invalid = input('Do you want to quit?(y/n): ').lower()
                            if invalid in ['y', 'yes']:
                                sys.exit()
                            else:
                                print('Please enter a valid command')

                    # If the user chooses to go left
                    elif choose_path == "left":
                        print('You fallen to a trap. YOU DIED')
                        status.dead(charac)

                    # Ask if they want to quit
                    else:
                        invalid = input('Do you want to quit?(y/n): ').lower()
                        if invalid in ['y', 'yes']:
                            sys.exit()
                        else:
                            print('Please enter a valid command')

            # if the user choose break
            elif choose_path == "break":
                print("You have no weapon, it will take time to break it")
                # Simulate that it is breaking the boulder
                for _ in range(5):
                    print("........")
                    time.sleep(2)
                print("You died in Exhaustion and Starvation ")
                status.dead(charac)

            else:
                invalid = input('Do you want to quit?(y/n): ').lower()
                if invalid in ['y', 'yes']:
                    sys.exit()
                else:
                    print('Please enter a valid command')

        while choose_path != "forward":
            # Classes that need in this gameplay
            potion = Potions()
            weapon = Weapon()
            trolls = Trolls()
            goblin = Goblins()
            dragon = Dragon()

            # Display
            print("\n-----------------------------------------------------------------")
            status.playing_stats(charac)
            print(f"\n\n\tThere is an Enemy. It is a {goblin.name} and {trolls.name}")
            print("\t\t\tFight\t\t\tRun")
            print("----------------------------------------------------------------")
            # Get user input
            choose_path = input("\n> ").lower()
            # IF use chooses to fight
            if choose_path == 'fight':
                fighting = True
                while fighting:
                    # Simulation of fighting
                    print("\n------------------------------------------------------")
                    status.playing_stats(charac)
                    print(f'\n\nYou attacked. It dealt {charac.attack} damage')
                    goblin.hp -= charac.attack
                    trolls.hp -= charac.attack

                    # Check if someone is dead
                    if goblin.hp <= 0 or trolls.hp <= 0:
                        fighting = False
                        print('Goblins are dead')
                        print("Trolls are dead")
                        # Continuing the Adventure
                        print("------------------------------------------------")
                        status.playing_stats(charac)
                        print("\n\n\tYou continued to walk and saw a two path")
                        print("\n\t\tLeft\t\tRight")
                        print("------------------------------------------------")
                        # Get user input
                        choose_path = input("\n> ").lower()
                        # IF user chooses to go left
                        if choose_path == "left":
                            print("------------------------------------------------")
                            status.playing_stats(charac)
                            print("\n\n\tYou found a potion.")
                            charac.hp += potion.hp
                            print("\n\n\tThere are two paths")
                            print("\n\t\tForward\t\tLeft")
                            print("------------------------------------------------")
                            # Get user input
                            choose_path = input("\n> ").lower()
                            # IF the user chooses to go left again
                            if choose_path == "left":
                                print("----------------------------------------------")
                                print("\nThere is a narrow path ahead")
                                print("\nYou want to go to that narrow path?")
                                print("----------------------------------------------")
                                # Get user input
                                choose_path = input("\n> ").lower()
                                # IF the user choose not go to the narrow path
                                if choose_path not in ['y', 'yes']:
                                    print("\nFiery Fiend appeared and grab you!")
                                    status.dead(charac)
                                # IF the user chooses to go to the narrow path
                                else:
                                    print("\nYou found new weapon!")
                                    weapon.attack += charac.attack
                                    for _ in range(5):
                                        print("\n.........")
                                        time.sleep(2)
                                    print("\nThere is a big cast shadow")
                                    print("ROOOAAAARR!")
                                    print("The Dragon appeared! You need to defeat the Dragon in order to retrieved the Morphia Jewels")

                                    # Simulate fighting
                                    ask = input("\nAttack or Run?:\n> ").lower()
                                    # IF the user chooses attack
                                    if ask == "attack":
                                        # Active flag
                                        fighting = True
                                        # Fighting loop
                                        while fighting:
                                            print("------------------------------------------------------------------------------------------------------")
                                            # Display the users stats
                                            status.playing_stats(charac)
                                            print(f"\nYou attacked and it dealt {charac.attack} damage ")
                                            dragon.hp -= charac.attack

                                            # Check if the health of dragon is equal to zero and display the user has won
                                            if dragon.hp <= 0:
                                                print("\nYou defeated the Dragon!!! You won! The villagers are happy because the Morphia Jewels are back.")
                                                play_again = input("\nDo you want to play again?(y/n): ").lower()

                                                # Ask user if they want to play again
                                                if play_again not in ['y', 'yes']:
                                                    sys.exit()
                                                else:
                                                    titlescreen()
                                            # IF the dragon is still alive
                                            else:
                                                # Display the stats of dragon
                                                print("\nt")
                                                status.playing_stats(dragon)
                                                print(f"\n\nThe Dragon attacked and it dealt {dragon.attack} damage!")
                                                charac.hp -= dragon.attack

                                                # Check if the user is dead
                                                if charac.hp <= 0:
                                                    fighting = False
                                                    status.dead(charac)
                                    # If the user chooses to run
                                    elif choose_path == "run":
                                        print("\nThe dragon blocked your way and attacked you")
                                        print("You pass out and became feast of the Dragon")
                                        status.dead(charac)
                                    # If the choose_path is invalid
                                    else:
                                        invalid = input('Do you want to quit?(y/n): ').lower()
                                        if invalid in ['y', 'yes']:
                                            sys.exit()
                                        else:
                                            print('Please enter a valid command')

                            # If the user choose Forward
                            elif choose_path == "forward":
                                print("\n......")
                                time.sleep(2)
                                print("BOOOGSH")
                                print("You fell into a trap.")
                                status.dead(charac)

                            # If the users choose_path is invalid
                            else:
                                invalid = input('Do you want to quit?(y/n): ').lower()
                                if invalid in ['y', 'yes']:
                                    sys.exit()
                                else:
                                    print('Please enter a valid command')
                        # If the user choose right after the fight
                        elif choose_path == "right":
                            for _ in range(5):
                                print(".....")
                                time.sleep(1)
                            print("BOOOOOGSH!")
                            print("Big Boulder fell on you")
                            status.dead(charac)
                        # If the users choose_path is invalid
                        else:
                            invalid = input('Do you want to quit?(y/n): ').lower()
                            if invalid in ['y', 'yes']:
                                sys.exit()
                            else:
                                print('Please enter a valid command')

                    else:
                        # Display the stats of fiery fiend
                        print("\n")  # Adding spaces
                        print(f'Goblins{status.playing_stats(goblin)}')
                        print(f'Trolls{status.playing_stats(trolls)}')
                        print(f'\n\nGoblin attacked. It dealt {goblin.attack} damage')
                        print(f'\n\nTrolls attacked. It dealt {trolls.attack} damage')
                        # Updating the status of the character
                        charac.hp -= goblin.attack
                        charac.hp -= trolls.attack
                        # Check if users hp is zero
                        if charac.hp <= 0:
                            fighting = False
                            status.dead(charac)
            # IF the user choose to run in fighting goblins and trolls
            elif choose_path == "run":
                print('\nGoblin heard you... Goblins and Trolls chase you and caught you...')
                print('You become their feast.\nYOU DIED!')
                status.dead(charac)
            # IF the user enter a invalid command
            else:
                invalid = input('Do you want to quit?(y/n): ').lower()
                if invalid in ['y', 'yes']:
                    sys.exit()
                else:
                    print('Please enter a valid command')


def titlescreen():
    """Creating a Title Screen"""
    print("|--------Welcome To Morphia------------|")
    print("|--------------Start-------------------|")
    print("|--------------Help--------------------|")
    print("|--------------Quit--------------------|")
    # Get user input
    choose = input('> ').lower()
    if choose == 'start':
        print("\n" * 100)
        choose_role()
    elif choose == 'help':
        helper()
    elif choose == 'quit':
        sys.exit()
    # If the choice of user is not in choices this code will run
    while choose not in ['start', 'help', 'quit']:
        print('Please enter a valid command')
        choose = input('> ').lower()
        if choose == 'start':
            choose_role()
        elif choose == 'help':
            helper()
        elif choose == 'quit':
            sys.exit()


def helper():
    """This function will run if user choose help"""
    print("|-------------------------------------|")
    print("| Just type the options that you want |")
    print("|      Goodluck and have fun          |")
    print("|-------------------------------------|")
    print('\nType back to go to the titlescreen.')
    goback = input('> ').lower()
    if goback in ['back', 'go back']:
        titlescreen()


def choose_role():
    choose_charac = "\nWelcome to the world of Morphia.\n\nPlease choose a Character.\nAssassin\nArcher\nWarrior"
    # Printing slowly
    for letter in choose_charac:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    # Get user input
    choice = input('\n> ').lower()

    if choice == 'assassin':
        name = input('\nWhat is the name of your character?: ').title()
        # Calling the class to access it
        assassin = Assassin(name)
        print(f'\nWelcome {assassin.name}!')
        # Displaying the stats
        status = Status()
        status.stats(assassin)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            play(assassin, status)

    elif choice == 'archer':
        name = input('\nWhat is the name of your character?: ').title()
        # Calling the Class to access it
        archer = Archer(name)
        print(f'\nWelcome {archer.name}!')
        # Displaying the stats
        status = Status()
        status.stats(archer)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            play(archer, status)

    elif choice == 'warrior':
        name = input('\nWhat is the name of your character?: ').title()
        # Calling the Class to access it
        warrior = Warrior(name)
        print(f'\nWelcome {warrior.name}!')
        # Displaying the stats
        status = Status()
        status.stats(warrior)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            play(warrior, status)

    else:  # If the choice is not in character
        print('\nPlease choose valid choice!')
        choose_role()


def main():
    titlescreen()


if __name__ == '__main__':
    main()

