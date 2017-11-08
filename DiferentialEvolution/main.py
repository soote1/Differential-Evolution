from DIFEVO.difEvoAlgorithm import DifEvoAlgorithm
from random import uniform


def main():
    scale_factor = uniform(0.4, 0.9)
    crossover_range = 0.9
    generations = 30
    population_size = 100
    dimensions = 10

    dif_evo_algorithm_helper = DifEvoAlgorithm(
        scale_factor,
        crossover_range,
        population_size,
        dimensions,
        generations
    )

    dif_evo_algorithm_helper.do_algorithm()


if __name__ == '__main__':
    main()
