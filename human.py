class Human():
	def __init__(self, piece):
		self.piece = piece
	def check_move(self, board, move):
		if(move[0] > 2 or move[0] < 0 or move[1] > 2 or move[1] < 0):
			return False
		elif(board[move[0]][move[1]] != " "):
			return False
		return True
	def get_move(self, board):
		row = int(input("enter row: "))
		col = int(input("enter col: "))
		while not self.check_move(board, [row - 1, col - 1]):
			print("Invalid move. Try again.")
			row = int(input("enter row: "))
			col = int(input("enter col: "))
		return [row - 1, col - 1]