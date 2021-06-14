#Dva igraca - na pocetku oba dobijaju po 4 zetona i unosi se niz celih brojeva koji mogu biti i negativni.
#Igra se naizmenicno - svaki igrac stavlja zeton na slobodno polje. Kada se odigraju svi potezi sabiraju se polja na kojima su zetoni.
#Pobednik je onaj igrac koji ima najvise poena u zbiru.


import copy
import random

class Game:
	def __init__(self):
		self.initialize_game()
		
	def initialize_game(self):
		self.current_state = [random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)]
		self.current_state_holder = [0, 0, 0, 0, 0, 0, 0, 0]
		self.zetoni_player = 4
		self.zetoni_computer = 4
		self.player_total = 0
		self.computer_total = 0
		self.player_turn = 1
		
	def evaluation(self, current_state_holder):
		tmp_player_total = self.player_total
		player_total_count = 4 - self.zetoni_player
		tmp_computer_total = self.computer_total
		computer_total_count = 4 - self.zetoni_computer
		for i in range(8):
			if self.current_state[i] != float('-inf'):
				if current_state_holder[i] == 1:
					tmp_player_total += self.current_state[i]
					player_total_count += 1
				elif current_state_holder[i] == 2:
					tmp_computer_total += self.current_state[i]
					computer_total_count += 1
		if player_total_count + computer_total_count == 8:
			if tmp_player_total > tmp_computer_total:
				return -1
			elif tmp_player_total < tmp_computer_total:
				return 1
			else:
				return 0
		else:
			return None
	
	def get_next_states(self, current_state_holder, player):
		next_states = []
		for i in range(8):
			if current_state_holder[i] == 0:
				if player == 1:
					next_state = copy.deepcopy(current_state_holder)
					next_state[i] = 1
					next_states.append((i, next_state))
				elif player == 2:
					next_state = copy.deepcopy(current_state_holder)
					next_state[i] = 2
					next_states.append((i, next_state))
		return next_states
	
	def Max(self, stanje, alpha, beta):
		state_value = self.evaluation(stanje)
		if state_value != None:
			return (state_value, None)
		v = float('-inf')
		max_i = None
		for (i, next_state) in self.get_next_states(stanje, 2):
			(value, min_i) = self.Min(next_state, alpha, beta)
			if v < value:
				v = value
				max_i = i
			if v >= beta:
				return (v, i)
			if v > alpha:
				alpha = v
		return (v, max_i)
	
	def Min(self, stanje, alpha, beta):
		state_value = self.evaluation(stanje)
		if state_value != None:
			return (state_value, None)
		v = float('inf')
		min_i = None
		for (i, next_state) in self.get_next_states(stanje, 1):
			(value, max_i) = self.Max(next_state, alpha, beta)
			if v > value:
				v = value
				min_i = i
			if v <= alpha:
				return (v, i)
			if v < beta:
				beta = v
		return (v, min_i)
		
	def play(self):
		self.draw_game_state()
		
		state_value = self.evaluation(self.current_state_holder)
		if state_value != None:
			if state_value == -1:
				print("Pobedio je igrac")
			elif state_value == 0:
				print("Izjednaceno je")
			elif state_value == 1:
				print("Pobedio je racunar")
			
			self.initialize_game()
			return
		
		if self.player_turn == 1:
			polje = int(input("Unesite polje na koje stavljate zeton: "))
			self.current_state_holder[polje] = 1
			self.player_total += self.current_state[polje]
			self.current_state[polje] = float('-inf')
			self.zetoni_player -= 1
			self.player_turn = 2
			self.play()
		else:
			(v, polje) = self.Max(self.current_state_holder, float('-inf'), float('inf'))
			self.current_state_holder[polje] = 2
			self.computer_total += self.current_state[polje]
			self.current_state[polje] = float('-inf')
			self.zetoni_computer -= 1
			self.player_turn = 1
			self.play()
	
	def draw_game_state(self):
		print("_________________________________")
		print("Broj zetona koje ima protivnik: {}".format(self.zetoni_computer))
		print("Broj poena koje ima protivnik: {}".format(self.computer_total))
		print("---------------------------------")
		print("Niz: {}".format(self.current_state))
		print("---------------------------------")
		print("Broj zetona koje ima igrac: {}".format(self.zetoni_player))
		print("Broj poena koje ima igrac: {}".format(self.player_total))
		print("_________________________________")
	
def main():
	game = Game()
	game.play()
if __name__ == "__main__":
	main()	
