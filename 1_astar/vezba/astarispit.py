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
		n = len(w)
		
    for i in range(n):
    	neighbor = w[:]
    	neighbor[i] = (neigbor[i] - 1 + 5) % 14 +1
			neighbors.append((self.serialize(neighbor), 1))
		return neighbors
    
	# Funkcija heuristicke procene udaljenosti od stanja v
	# do ciljnog stanja
	def h(self, v):
		w = self.deserialize(v)
		n = len(w)
		m = len(set(w))
		return n-m
    
	# Funkcija pronalazi put od start stanja do ciljnog stanja
	# koriscenjem a* algoritma
	def astar(self, start):
		open_list = set([self.serialize(start)])
		closed_list = set([])
		
		g = dict([])
		g[self.serialize(start)] = 0
		
		parent = dict([])
		parent[self.serialize(start)] = self.serialize(start)
		
		while len(open_list) > 0:
			min_distance = float('inf')
			n = None
			
			for v in open_list:
				if g[v] + self.h(v) < min_distance:
					min_distance = g[v] + self.h(v)
					n = v
					
			if set(self.deserialize(n)) = {1}:
				print(n)
				path = []
				while n != parent[n]:
					path.append(self.deserialize(n))
					n = parent[n]
				path.append(start)
				path.reverse()
				return path
			
			for (m, weight) in self.get_neighbors(n):
				if m not in open_list and m not in closed_list:
					open_list.add(m)
					g[m] = g[n] + weight
					parent[str(m)] = n
				else:
					if g[n] + weight + self.h(m) < g[m] + self.h(m):
						g[m] = g[n] + weight
						parent[m] = n
						if m in closed_list:
							closed_list.remove(m)
							open_list.add(m)
        
		print('Put nije pronadjen!')
		return None
        
g = Graph()
g.astar([5,10,1])
