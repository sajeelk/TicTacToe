
class Bot():
	def __init__(self, piece):
		self.piece = piece
		self.opp = "O" if piece == "X" else "X"
	
	def check_draw(self, board):
		for i in range(3):
			for j in range(3):
				if(board[i][j] == " "):
					return False
		return True
	def check_win(self, board):
		# returns the winner or None if none
		for col in range(3):
			if(board[0][col] == board[1][col] == board[2][col] != " "):
				return board[0][col]
		for row in range(3):
			if(board[row][0] == board[row][1] == board[row][2] != " "): 
				return board[row][0]
		if(board[0][0] == board [1][1] == board[2][2] != " "):
			return board[0][0]
		elif(board[0][2] == board[1][1] == board[2][0] != " "):
			return board[0][2]
		return None

	
	def minimax(self, board, myTurn, depth, a, b):
		if(self.check_win(board) == self.piece):
			return 10 - depth
		if(self.check_win(board) == self.opp):
			return -10 + depth
		if(self.check_draw(board)):
			return 0
		if(myTurn):
			value = -1000
			for i in range(3):
				for j in range(3):
					if board[i][j] == " ":
						board[i][j] = self.piece
						value = max(value, self.minimax(board, False, depth + 1, a, b))
						board[i][j] = " "
						if value >= b:
							return value
						if value > a:
							a = value
			return value - depth
		else:
			value = 1000
			for i in range(3):
				for j in range(3):
					if board[i][j] == " ":
						board[i][j] = self.opp
						value = min(value, self.minimax(board, True, depth + 1, a, b))
						board[i][j] = " "
						if value <= a:
							return value
						if value < b:
							b = value
			return value + depth
	def get_move(self, board):
		soard = [[-100, -100, -100],[-100, -100, -100],[-100, -100, -100]]
		for i in range(3):
			for j in range(3):
				if board[i][j] == " ":
					board[i][j] = self.piece
					score = self.minimax(board, False, 0, -1000, 1000)
					soard[i][j] = score
					board[i][j] = " "
		maxScore = -1000
		best_move = []
		for i in range(3):
			for j in range(3):
				if soard[i][j] >= maxScore:
					maxScore = soard[i][j]
					best_move = [i, j]
		return best_move