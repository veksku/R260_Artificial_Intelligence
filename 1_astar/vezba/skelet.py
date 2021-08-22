class Graph:
        
	# Funkcija pretvara listu v u tekstualni oblik
	# [1,2,3] -> "1,2,3"
	def serialize(self, v):
		return ','.join([str(x) for x in v])
    
	# Funkcija pretvara v iz tekstualnog oblika u listu
	# "1,2,3" -> [1,2,3]
	def deserialize(self, v):
		return [int(x) for x in v.split(',')]
        
	# Funkcija vraca niz susednih stanja u obliku (w, e)
	# gde je w susedno stanje a e duzina grane od cvora v
	# do cvora w
	def get_neighbors(self, v):
		w = self.deserialize(v)
		neighbors = []


			neighbors.append((self.serialize(neighbor), 1))
		return neighbors
    
	# Funkcija heuristicke procene udaljenosti od stanja v
	# do ciljnog stanja
	def h(self, v):
		w = self.deserialize(v)

    
	# Funkcija pronalazi put od start stanja do ciljnog stanja
	# koriscenjem a* algoritma
	def astar(self, start):
	
	   
		print('Put nije pronadjen!')
		return None
        
g = Graph()
g.astar([5,10,1])
