import random

class Individual():
	def __init__(self, size, target): 
		self.target = target
		self.size = size
		self.code = [random.choice([0, 1]) for _ in range(self.size)] #niz code koji ima nule i jedinice i oznacava koju jedinku koristimo u dostizanju 'target'-a
		self.fitness = self.calculateFitness() #funkcija koja ce odrediti naj jedinku
		
	def __lt__(self, other):
		return self.fitness < other.fitness #pomocna funkcija za sort kasnije
		
	def calculateFitness(self): 
		broj_odstupanja = self.size
		for i in range(self.size):
			if self.code[i] == self.target[i]:
				broj_odstupanja -= 1
		return broj_odstupanja	
		
	def mutation(self, mutation_rate):
		x = random.uniform(0, 1) # x = (0,1)
		if x < mutation_rate: #ako je x manji od konstante za mutaciju
			index = random.randint(0, self.size-1) #random indeks
			self.code[index] = 1 if self.code[index] == 0 else 0 #mutiraj random indeks code-a
			self.fitness = self.calculateFitness() #racunaj fitness
	
def selection(population, size): #biramo 'size' broj jedinki od kojih biramo onu s najboljim fitnessom
	minFitness = 11
	bestIndex = -1
	for i in range(size):
		index = random.randrange(len(population))
		if population[index].fitness < minFitness:
			minFitness = population[index].fitness
			bestIndex = index
	return bestIndex
	
def crossover(parent1, parent2, target): #ukrsta dve jedinke i stvara novu
	child1 = Individual(10, target)
	child2 = Individual(10, target)
	
	breakpoint = random.randrange(10) #delimo jedinku na dva dela, podela je random
	child1.code[:breakpoint] = parent1.code[:breakpoint] #prvi deo prve je prvi deo prvog roditelja
	child1.code[breakpoint:] = parent2.code[breakpoint:] #drugi deo prve je drugi deo drugog roditelja
	
	child2.code[:breakpoint] = parent2.code[:breakpoint] #prvi deo druge je prvi deo drugog roditelja
	child2.code[breakpoint:] = parent1.code[breakpoint:] #drugi deo druge je drugi deo prvog roditelja
	
	child1.fitness = child1.calculateFitness()
	child2.fitness = child2.calculateFitness()
	
	return (child1, child2)

TOURNAMENT_SIZE = 12 #broj jedinki koje ce da ucestvuju u selection funkciji
POPULATION_SIZE = 30
ELITISM_SIZE = int(0.2 * POPULATION_SIZE)	#najbolje jedinke
MAX_ITER = 500
MUTATION_RATE = 0.03 #odredjuje koliko cesto ce se do kraja izvrsiti mutation funkcija

target = [1, 1, 1, 0, 1, 1, 1, 0, 1, 1] #zeljeno resenje

population = [Individual(10, target) for i in range(POPULATION_SIZE)]
newPopulation = [Individual(10, target) for i in range(POPULATION_SIZE)]

for i in range(MAX_ITER):
	population.sort()
	print("Trenutni najbolji " + str(population[0].code))
	if population[0].fitness == 0:
		break
	newPopulation[:ELITISM_SIZE] = population[:ELITISM_SIZE] #prvih ELITISM_SIZE najboljih kopiramo
	for j in range(ELITISM_SIZE, POPULATION_SIZE, 2): #gazimo sve ostale posle ELITISM_SIZE
		parent1index = selection(population, TOURNAMENT_SIZE)
		parent2index = selection(population, TOURNAMENT_SIZE)

		child1, child2 = crossover(population[parent1index], population[parent2index], target)
		child1.mutation(MUTATION_RATE)
		child2.mutation(MUTATION_RATE)
		
		newPopulation[j] = child1
		newPopulation[j+1] = child2
		
	population = newPopulation #dodela da bi se moglo nastaviti iterativno izvrsavanje algoritma

#bestIndividual = min(population, key=lambda x: x.fitness)
#print(bestIndividual.code)
bestIndividual = population[0]
print("Najbolje resenje posle " + str(i) + " iteracija/e: " + str(bestIndividual.code))
