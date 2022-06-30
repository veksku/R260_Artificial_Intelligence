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
		#=========================
		fitness = self.size
		for i in range(self.size):
			if self.code[i] == self.target[i]:
				fitness -= 1
		return fitness
		#=========================
	def mutation(self, mutation_rate):
		#=========================
		x = random.uniform(0,1)
		if x < MUTATION_RATE:
			index = random.randrange(0,self.size)
			self.code[index] = 0 if self.code[index] == 1 else 1
			self.fitness = self.calculateFitness()
		#=========================

	
def selection(population, size):
	#=========================
	minFitness = 11
	bestIndex = -1
	for i in range(size):
		index = random.randrange(len(population))
		if population[index].fitness < minFitness:
			minFitness = population[index].fitness
			bestIndex = index
	return bestIndex
	#=========================
	
#ruletska selekcija
#=========================
#def roulette(population)
#	total_fitness = sum([x.fitness for x in population])
#	random = random.random()
#	current_sum = 0
#	for i in range(population.size()):
#		current_sum += population[i].fitness
#		if current_sum > random:
#			return population[i]
#=========================
	
	
def crossover(parent1, parent2, target):
	#=========================
	child1 = Individual(len(target), target)
	child2 = Individual(len(target), target)
	
	breakpoint = random.randrange(0, len(target))
	child1.code[:breakpoint] = parent1.code[:breakpoint]
	child1.code[breakpoint:] = parent2.code[breakpoint:]
	
	child2.code[:breakpoint] = parent2.code[:breakpoint]
	child2.code[breakpoint:] = parent1.code[breakpoint:]
	
	child1.fitness = child1.calculateFitness()
	child2.fitness = child2.calculateFitness()
	
	return (child1, child2)
	#=========================


TOURNAMENT_SIZE = 6
POPULATION_SIZE = 25 
ELITISM_SIZE = int(0.3 * POPULATION_SIZE)
MAX_ITER = 500
MUTATION_RATE = 0.01

target = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]

population = [Individual(10, target) for i in range(POPULATION_SIZE)]
newPopulation = [Individual(10, target) for i in range(POPULATION_SIZE)]

for i in range(MAX_ITER):
	#=========================
	population.sort()
	if population[0].fitness == 0:
		break
	newPopulation[:ELITISM_SIZE] = population[:ELITISM_SIZE]
	for j in range(ELITISM_SIZE, POPULATION_SIZE, 2):
		indexParent1 = selection(population, TOURNAMENT_SIZE)
		indexParent2 = selection(population, TOURNAMENT_SIZE)
		
		(child1, child2) = crossover(population[indexParent1], population[indexParent2], target)
		
		child1.mutation(MUTATION_RATE)
		child2.mutation(MUTATION_RATE)
		
		newPopulation[j] = child1
		newPopulation[j+1] = child2
	#=========================
	population = newPopulation
	
bestIndividual = population[0]
print(bestIndividual.code)
