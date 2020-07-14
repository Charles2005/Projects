import random
import math
import tkinter


class Simulation:
    def __init__(self):
        """Simulation of the App"""
        # Number of days
        self.day_number = 1

        # Getting user input for the population size
        print('To simulate the an epidemic outbreak, we must know the population size.')
        population = int(input('Enter the population size: '))
        self.population_size = population

        # Creating a Visual
        root = math.sqrt(self.population_size)

        if int(root + .5) ** 2 != self.population_size:
            round(root, 0)
            self.grid_size = int(root)
            self.population_size = self.grid_size ** 2
            print(f'Rounding population size to {self.population_size} for visual purposes')
        else:
            self.grid_size = int(math.sqrt(self.population_size))


        # Getting the percentage of the population
        print('\nWe must first start by infecting a portion of the population')
        percent = int(input('Enter the percentage (0-100) of the population to initially infect: ')) / 100
        self.infection_percent = percent

        # Getting the probability
        print('\nWe must know the risk a person has to contract the disease when exposed')
        proba = int(input('Enter the probabilty (0-100) that a person gets infected when exposed to the disease: '))
        self.infection_probability = proba

        # Getting how long the infection will last
        print('\nWe must know how long the infection will last when exposed.')
        time = int(input('Enter the duration (in days) of the infection: '))
        self.infection_duration = time

        # Getting the mortality rate of those infected
        print('\nWe must know the mortality rate of those infected.')
        mor_rate = int(input('Enter mortality rate(0-100) of the infection: '))
        self.mortality_rate = mor_rate

        # Getting how long the simulation going to take
        print('\nWe must know how long to run the simulation.')
        duration = int(input('Enter the number of days to simulate: '))
        self.sim_days = duration


class Person:
    def __init__(self):
        """Initialize the person class"""
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        """Creating a method for infecting"""
        infected = random.randint(0, 100)
        if infected < sim.infection_probability:
            self.is_infected = True

    def heal(self):
        """Method for heal"""
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        """Check if the person is dead"""
        self.is_dead = True

    def update(self, sim):
        """Updating the simulation"""
        # Check if the person is dead
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
            # CHeck if the mortality rate is high or low
            if random.randint(0, 100) < sim.mortality_rate:
                self.die()
            # if the person is not dead it will heal the person
            elif self.days_infected == sim.infection_duration:
                self.heal()


class Population:
    def __init__(self, sim):
        self.population = []

        for i in range(sim.grid_size):
            row = []
            for y in range(sim.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, sim):
        """Method to see the initial infected"""
        infected_count = int(round(sim.infection_percent * sim.population_size, 0))
        # Creating visual
        infections = 0
        while infections < infected_count:
            x = random.randint(0, sim.grid_size - 1)
            y = random.randint(0, sim.grid_size - 1)

             # if the person is not infected
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self, sim):
        """Spreading the virus"""
        for i in range(sim.grid_size):
            for o in range(sim.grid_size):
                if self.population[i][o].is_dead == False:
                    # if the person is not dead
                    if i == 0:
                        if o == 0:
                            if self.population[i][o + 1].is_infected or  self.population[i + 1][o].is_infected:
                                self.population[i][o].infect(sim)

                            elif o == sim.grid_size - 1:
                                if self.population[i][o - 1].is_infected or self.population[i + 1][o].is_infected:
                                    self.population[i][o].infect(sim)

                            else:
                                if self.population[i][o - 1].is_infected or self.population[i][o + 1].is_infected or \
                                        self.population[i + 1][o].is_infected:
                                    self.population[i][o].infect(sim)

                        elif i == sim.grid_size - 1:
                            if o == 0:
                                if self.population[i][o + 1].is_infected or self.population[i - 1][o].is_infected:
                                    self.population[i][o].infect(sim)

                                elif o == sim.grid_size - 1:

                                    if self.population[i][o - 1].is_infected or self.population[i - 1][o].is_infected:
                                        self.population[i][o].infect(sim)

                                else:

                                    if self.population[i][o - 1].is_infected or self.population[i][o + 1].is_infected \
                                    or self.population[i - 1][o].is_infected:

                                        self.population[i][o].infect(sim)
                        else:
                            if o == 0:

                                if self.population[i][o + 1].is_infected or self.population[i + 1][o].is_infected or \
                                        self.population[i - 1][o].is_infected:

                                    self.population[i][o].infect(sim)

                                elif o == sim.grid_size - 1:
                                    if self.population[i][o - 1].is_infected or self.population[i + 1][o].is_infected or \
                                            self.population[i - 1][o].is_infected:

                                        self.population[i][o].infect(sim)
                                else:
                                    if self.population[i][o - 1].is_infected or self.population[i][o + 1].is_infected or \
                                            self.population[i + 1][o].is_infected or \
                                            self.population[i - 1][o].is_infected:

                                        self.population[i][o].infect(sim)

    def update(self, sim):
        """Update the simulation"""
        sim.day_number += 1
        for row in self.population:
            for person in row:
                person.update(sim)

    def display_statistics(self, sim):
        """Method for displaying the statistics"""
        total_infected = 0
        total_death = 0
        # loop through the population list
        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected += 1
                    if person.is_dead:
                        total_death += 1
        # Creating infection percentage
        infected_percent = round(100 * (total_infected / sim.population_size), 4)
        death_percent = round(100 * (total_death / sim.population_size), 4)

        # Displaying the summary
        print(f'\n---Day # {sim.day_number}---')
        print(f'Percentage of Population Infected: {infected_percent}%')
        print(f'Percetage of Population Dead: {death_percent}%')
        print(f'Total People Infected: {total_infected}/{sim.population_size}')
        print(f'Total People Deaths: {total_death}/{sim.population_size}')


def graphic(simulation, population, canvas):
    """Creating the graphics"""
    square_dimension = 600//simulation.grid_size

    for i in range(simulation.grid_size):
        y = i * square_dimension

        for o in range(simulation.grid_size):
            x = o * square_dimension

            if population.population[i][o].is_dead:
                canvas.create_rectangle(x, y, x + square_dimension, y + square_dimension, fill ='red')

            else:
                if population.population[i][o].is_infected:
                    canvas.create_rectangle(x, y, x + square_dimension, y + square_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x, y, x + square_dimension, y + square_dimension, fill='green')


def main():
    """Main algo"""
    sim = Simulation()

    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    sim_window = tkinter.Tk()
    sim_window.title('Epidemic Outbreak')
    sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height = WINDOW_HEIGHT, bg='lightblue')
    sim_canvas.pack(side=tkinter.LEFT)

    population = Population(sim)

    population.initial_infection(sim)
    population.display_statistics(sim)
    input("\nPress Enter to begin the simulation.")

    # Loop to simulate each day
    for i in range(1, sim.sim_days):
        population.spread_infection(sim)
        population.update(sim)
        population.display_statistics(sim)
        graphic(sim, population, sim_canvas)

        sim_window.update()

        if i != sim.sim_days - 1:

            sim_canvas.delete('all')


main()








