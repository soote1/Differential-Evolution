from DIFEVO.individual import Individual
from random import uniform, randint

from DIFEVO.vectorArithmetic import VectorArithmetic


class DifEvoAlgorithm:

    def __init__(self, scale_factor, crossover_range, population_size, dimensions, generations):
        self.scaleFactor = scale_factor
        self.crossoverRange = crossover_range
        self.populationSize = population_size
        self.dimensions = dimensions
        self.generations = generations
        self.population = []

    def do_algorithm(self):
        self.init_population()
        self.main_process()

    def init_population(self):
        self.population = [Individual() for i in range(0, self.populationSize)]

        for i in range(0, len(self.population)):
            for j in range(0, self.dimensions):
                random_value = self.get_random_value(-5, 5)
                self.population[i].set_position_in_dimension(random_value)

    def main_process(self):
        for g_index in range(0, self.generations):
            for p_index in range(0, self.populationSize):

                current_position = self.population[p_index].get_position()

                r1 = randint(0, self.populationSize-1)

                while True:
                    r2 = randint(0, self.populationSize-1)
                    if r2 != r1:
                        break

                while True:
                    r3 = randint(0, self.populationSize-1)
                    if r3 != r2 and r3 != r1:
                        break

                mutant_vector = self.get_mutant_vector(r1, r2, r3)

                random_individual = randint(0, self.populationSize-1)

                new_position = [0] * self.dimensions

                for d_index in range(0, self.dimensions):
                    rcj = self.get_random_value(0, 1)
                    if rcj < self.crossoverRange or d_index == random_individual:
                        new_position[d_index] = mutant_vector[d_index]
                    else:
                        new_position[d_index] = current_position[d_index]

                new_position_fitness = VectorArithmetic.sphere_function(new_position)
                current_position_fitness = VectorArithmetic.sphere_function(current_position)

                if new_position_fitness < current_position_fitness:
                    self.population[p_index].set_position(new_position)

            if g_index == 0 or g_index == 14 or g_index == 29:
                self.print_results(g_index)

    def print_results(self, g_index):
        str_result = ""

        str_result += "Generation #" + str(g_index+1) + "\n"
        for p_index in range(0, self.populationSize):
            str_result += "Individual #" + str(p_index) + "\n"
            pos = self.population[p_index].get_position()
            for d_index in range(0, self.dimensions):
                str_result += str(pos[d_index]) + ", "

            str_result += "\n"

        print(str_result)

    def get_mutant_vector(self, r1, r2, r3):
        r2_r3_difference = VectorArithmetic.subtraction(
            self.population[r2].get_position(),
            self.population[r3].get_position())

        scale_factor_applied = VectorArithmetic.vector_by_scalar(r2_r3_difference, self.scaleFactor)

        mutant_vector = VectorArithmetic.addition(self.population[r1].get_position(), scale_factor_applied)

        return mutant_vector

    @staticmethod
    def get_random_value(from_value, to_value):

        return uniform(from_value, to_value)
