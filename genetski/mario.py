import random

class Individual():
	def __init__(self, size, target):
		self.target = target
		self.size = size
		self.code = [random.choice([0, 1]) for _ in range(self.size)]
		self.fitness = self.calculateFitness()
		
	def __lt__(self, other):
		return self.fitness < other.fitness
		
	def calculateFitness(self):
		broj_odstupanja = self.size
		for i in range(self.size):
			if self.code[i] == self.target[i]:
				broj_odstupanja -= 1
		return broj_odstupanja	
		
	def mutation(self, mutation_rate):
		x = random.uniform(0, 1)
		if x < mutation_rate:
			index = random.randint(0, self.size-1)
			self.code[index] = 1 if self.code[index] == 0 else 0
			self.fitness = self.calculateFitness()
	
def selection(population, size):
	minFitness = 11
	bestIndex = -1
	for i in range(size):
		index = random.randrange(len(population))
		if population[index].fitness < minFitness:
			minFitness = population[index].fitness
			bestIndex = index
	return bestIndex
	
def crossover(parent1, parent2, target):
	child1 = Individual(10, target)
	child2 = Individual(10, target)
	
	breakpoint = random.randrange(10)
	child1.code[:breakpoint] = parent1.code[:breakpoint]
	child1.code[breakpoint:] = parent2.code[breakpoint:]
	
	child2.code[:breakpoint] = parent2.code[:breakpoint]
	child2.code[breakpoint:] = parent1.code[breakpoint:]
	
	child1.fitness = child1.calculateFitness()
	child2.fitness = child2.calculateFitness()
	
	return (child1, child2)

TOURNAMENT_SIZE = 6
POPULATION_SIZE = 25
ELITISM_SIZE = int(0.3 * POPULATION_SIZE)	
MAX_ITER = 500
MUTATION_RATE = 0.02

target = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]

population = [Individual(10, target) for i in range(POPULATION_SIZE)]
newPopulation = [Individual(10, target) for i in range(POPULATION_SIZE)]

for i in range(MAX_ITER):
	population.sort()
	print(population[0].code)
	if population[0].fitness == 0:
		break
	newPopulation[:ELITISM_SIZE] = population[:ELITISM_SIZE]
	for j in range(ELITISM_SIZE, POPULATION_SIZE, 2):
		parent1index = selection(population, TOURNAMENT_SIZE)
		parent2index = selection(population, TOURNAMENT_SIZE)

		child1, child2 = crossover(population[parent1index], population[parent2index], target)
		child1.mutation(MUTATION_RATE)
		child2.mutation(MUTATION_RATE)
		
		newPopulation[j] = child1
		newPopulation[j+1] = child2
		
	population = newPopulation

bestIndividual = min(population, key=lambda x: x.fitness)
print(bestIndividual.code)
