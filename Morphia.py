import random
import sys
import time


# Characters or Roles
class Assassin:
    def __init__(self, name):
        self.name = name
        self.hp = 75
        self.mp = 35
        self.attack = 80

    def stealth(self):
        damage = random.randint(20, 40)
        self.mp -= 10
        print(f'\n{self.name} used Stealth it dealt {damage} damage.')

    def smokescreen(self):
        self.mp -= 20
        print(f'\n{self.name} used Smokescreen, {self.name} is invulnerable.')

    def dancing_sword(self):
        damage = random.randint(50, 80)
        self.mp -= 30
        print(f'\n{self.name} used Dancing Sword it dealt {damage} damage.')


class Warrior:
    def __init__(self, name):
        self.name = name
        self.hp = 80
        self.mp = 50
        self.attack = 40

    def forward_slash(self):
        damage = random.randint(20, 40)
        self.mp -= 10
        print(f'\n{self.name} used Forward Slash it dealt {damage} damage.')

    def vanguard(self):
        self.mp -= 20
        print(f'\n{self.name} used Vanguard, {self.name} is invulnerable.')

    def judgement_call(self):
        damage = random.randint(50, 80)
        self.mp -= 30
        print(f'\n{self.name} used Judment Call it dealt {damage} damage.')


class Mage:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.mp = 80
        self.attack = 35

    def fiery_pit(self):
        damage = random.randint(40, 60)
        self.mp -= 20
        print(f'\n{self.name} used Fiery Pit it dealt {damage} damage.')

    def angel_blessing(self):
        self.mp += 30
        print(f'\n{self.name} used Angel Blessing, {self.name} restored 30 mp.')

    def element_storm(self):
        damage = random.randint(70, 120)
        self.mp -= 50
        print(f'\n{self.name} used element_storm it dealt {damage} damage.')

# Enemy


class Trolls:
    def __init__(self):
        self.name = 'Trolls'
        self.hp = random.randint(50, 100)
        self.attack = random.randint(15, 30)


class Goblins:
    def __init__(self):
        self.name = 'Goblins'
        self.hp = random.randint(70, 120)
        self.attack = random.randint(20, 40)


class FieryFiend:
    def __init__(self):
        self.name = 'Fiery Fiend'
        self.hp = random.randint(80, 150)
        self.attack = random.randint(40, 70)


class Dragon:
    def __init__(self):
        self.name = 'Dragon'
        self.hp = random.randint(100, 200)
        self.attack = random.randint(70, 100)


# Item
class Potions:
    def __init__(self):
        self.name = 'Potions'
        self.hp = random.randint(20, 50)
        self.mp = random.randint(30, 50)


# Weapons
class DivineKukri:
    def __init__(self):
        self.name = 'Divine Kukri'
        self.attack = random.randint(50, 100)


class GloriousHammerAndShield:
    def __init__(self):
        self.name = 'Glorious Hammer and Shield'
        self.health = random.randint(30, 50)
        self.attack = random.randint(30, 50)


class MysticWand:
    def __init__(self):
        self.name = 'Mystic Wand'
        self.attack = random.randint(15, 30)
        self.mp = random.randint(30, 60)


class Status:
    def __init__(self):
        self.dead = False

    @staticmethod
    def assassin_stats(assassin):
        print('\nThis are your stats')
        print(f'Attack: {assassin.attack} damage')
        print(f'Health: {assassin.hp} hp')
        print(f'Mana: {assassin.mp} mp')

    @staticmethod
    def mage_stats(mage):
        print('\nThis are your stats')
        print(f'Attack: {mage.attack} damage')
        print(f'Health: {mage.hp} hp')
        print(f'Mana: {mage.mp} mp')

    @staticmethod
    def warrior_stats(warrior):
        print('\nThis are your stats')
        print(f'Attack: {warrior.attack} damage')
        print(f'Health: {warrior.hp} hp')
        print(f'Mana: {warrior.mp} mp')

    def dead(self, charac):
        if charac.health == 0:
            self.dead = True
            print("\nYou're dead")
            play_again = input('\nDo you want to play again?(y/n): ').lower()
            if play_again not in ['y', 'yes']:
                sys.exit()
            else:
                titlescreen()


def assassin_play():
    pass


def mage_play():
    pass


def warrior_play():
    pass


def titlescreen():
    """Creating a Title Screen"""
    print("|--------Welcome To Morphia-------------|")
    print("|--------------Start--------------------|")
    print("|--------------Help--------------------|")
    print("|--------------Quit--------------------|")
    # Get user input
    choose = input('> ').lower()
    if choose == 'start':
        play()
    elif choose == 'help':
        helper()
    elif choose == 'quit':
        sys.exit()
    # If the choice of user is not in choices this code will run
    while choose not in ['start', 'help', 'quit']:
        print('Please enter a valid command')
        choose = input('> ').lower()
        if choose == 'start':
            play()
        elif choose == 'help':
            helper()
        elif choose == 'quit':
            sys.exit()


def helper():
    """This function will run if user choose help"""
    print("|-------------------------------|")
    print("| Just type the options that you want |")
    print("|      Goodluck and have fun         |")
    print("|-------------------------------|")
    print('\nType back to go to the titlescreen.')
    goback = input('> ').lower()
    if goback in ['back', 'go back']:
        titlescreen()


def play():
    choose_charac = "\nWelcome to the world of Morhphia.\n\nPlease choose a Character.\nAssassin\nMage\nWarrior"
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
        status.assassin_stats(assassin)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            assassin_play()

    elif choice == 'mage':
        name = input('\nWhat is the name of your character?: ').title()
        # Calling the Class to access it
        mage = Mage(name)
        print(f'\nWelcome {mage.name}!')
        # Displaying the stats
        status = Status()
        status.mage_stats(mage)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            mage_play()

    elif choice == 'warrior':
        name = input('\nWhat is the name of your character?: ').title()
        # Calling the Class to access it
        warrior = Warrior(name)
        print(f'\nWelcome {warrior.name}!')
        # Displaying the stats
        status = Status()
        status.warrior_stats(warrior)
        ask = input('\nAre you ready to start your quest? (y/n): ')
        # This will start the adventure
        if ask != 'y':
            sys.exit()
        else:
            warrior_play()

    else:  # If the choice is not in character
        print('\nPlease choose valid choice!')
        play()


def main():
    titlescreen()


main()










