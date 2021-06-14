import copy
import random

class Game:
	def __init__(self):
		self.initialize_game()
		
	def initialize_game(self):
		self.current_state = [random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100), random.randint(-100,100)]
		self.player_turn = 1
		self.zetoni_player = 4
		self.zetoni_computer = 4
		self.player_total = 0
		self.computer_total = 0
		
	def evaluation(self, current_state):
		if self.zetoni_player + self.zetoni_computer == 0:
			if self.player_total > self.computer_total:
				return -1
			elif self.player_total < self.computer_total:
				return 1
			elif self.player_total == self.computer_total:
				return 0
		else:
			return None
	
	def get_next_states(self, current_state, player, total):
		next_states = []
		for i in range(8):
			if current_state[i] != float('-inf'):
				if player == 1:
					next_state = copy.deepcopy(current_state)
					next_state[i] = float('-inf')
					next_player_total = total + current_state[i]
					#############################
				else:
					next_state = copy.deepcopy(current_state)
					next_state[i] = float('-inf')
					next_computer_total = total + current_state[i]
					#############################
		return next_states
			
	def Max(self, current_state, alpha, beta):
		state_value = self.evaluation(current_state)
		if state_value != None:
			return (state_value, None, None)
		v = float('-inf')
		max_i = None
		for (i,next_state) in self.get_next_states(current_state, 2, self.computer_total):
			(value, min_i) = self.Min(next_state, alpha, beta)
			if v < value:
				v = value
				max_i = i
			if v >= beta:
				return (v, i)
			if v > alpha:
				alpha = v
		return (v, max_i)
		
	def Min(self, current_state, alpha, beta):
		state_value = self.evaluation(current_state)
		if state_value != None:
			return (state_value, None, None)
		v = float('inf')
		min_i = None
		for (i, next_state) in self.get_next_states(current_state, 1, self.player_total):
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
		
		state_value = self.evaluation(self.current_state)
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
			self.player_total += self.current_state[polje]
			self.zetoni_player -= 1
			self.current_state[self.polje] = float('-inf')
			self.player_turn = 2
			self.play()
		else:
			(v, polje) = self.Max(self.current_state, float('-inf'), float('inf'))
			self.current_state[polje] = float('-inf')
			self.computer_total += self.current_state[polje]
			self.zetoni_computer -= 1
			self.player_turn = 1
			self.play()
			
	
	def draw_game_state(self):	
		print("Broj zetona koje ima protivnik: {}".format(self.zetoni_computer))
		print("Broj poena koje ima protivnik: {}".format(self.computer_total))
		print("---------------------------------")
		print("Niz: {}".format(self.current_state))
		print("---------------------------------")
		print("Broj zetona koje ima igrac: {}".format(self.zetoni_player))
		print("Broj poena koje ima igrac: {}".format(self.player_total))
		
def main():
	print("Igra pocinje")
	game = Game()
	game.play()
if __name__ == "__main__":
	main()
