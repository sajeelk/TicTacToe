import random 
class RandomBot():
	def __init__(self, piece):
		self.piece = piece
	def check_move(self, board, move):
		if(move[0] > 2 or move[0] < 0 or move[1] > 2 or move[1] < 0):
			return False
		elif(board[move[0]][move[1]] != " "):
			return False
		return True
	def get_move(self, board):
		m = [random.randint(0,2), random.randint(0,2)]
		while not self.check_move(board, m):
			m = [random.randint(0,2), random.randint(0,2)]
		return m