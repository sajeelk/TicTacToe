### TIC-TAC-TOE
from bot import Bot
from randombot import RandomBot
from human import Human
import sys

def print_board(board):
	print("\n   1   2   3\n       ")
	for i in range(3):
		print(str(i+1) + "  ", end="")
		for j in range(3):
			print(board[i][j], end=(" | " if j != 2 else ""))
		print("\n  -----------" if i != 2 else "\n")

def check_win(board):
	def check_col_win(board):
		for col in range(3):
			if(board[0][col] == board[1][col] == board[2][col] != " "):
				return board[0][col]
	
	def check_row_win(board):
		for row in range(3):
			if(board[row][0] == board[row][1] == board[row][2] != " "): 
				return board[row][0]
	
	def check_diagonal_win(board):    
		if(board[0][0] == board [1][1] == board[2][2] != " "):
			return board[0][0]
		elif(board[0][2] == board[1][1] == board[2][0] != " "):
			return board[0][2]

	def check_draw(board):
		for i in range(3):
			for j in range(3):
				if(board[i][j] == " "):
					return False
		return True

	if(check_diagonal_win(board)):
		return check_diagonal_win(board)
	if(check_row_win(board)):
		return check_row_win(board)
	if(check_col_win(board)):
		return check_col_win(board)
	if(check_draw(board)):
		return "Draw :)"
	return None

def menu():
	print("choose player 1:")
	print("Human, Easy Bot, Impossible Bot")
	p1_type = input("enter one of (human, easy, impossible): ").upper()
	while p1_type not in ["HUMAN", "EASY", "IMPOSSIBLE"]:
		p1_type = input("huh? make sure you enter one of these: (human, easy, impossible). try again: ").upper()

	
	print("choose player 2:")
	print("Human, Easy Bot, Impossible Bot")
	p2_type = input("enter one of (human, easy, impossible): ").upper()
	while p2_type not in ["HUMAN", "EASY", "IMPOSSIBLE"]:
		p2_type = input("huh? make sure you enter one of these: (human, easy, impossible). try again: ").upper()

	
	p1 = [Human("X"), RandomBot("X"), Bot("X")][["HUMAN", "EASY", "IMPOSSIBLE"].index(p1_type)]
	p2 = [Human("O"), RandomBot("O"), Bot("O")][["HUMAN", "EASY", "IMPOSSIBLE"].index(p2_type)]
	return [p1, p2]

def new_game(board, winner, p1, p2):
	print(("%s won!!!!!!!!!!!" % winner) if winner != "Draw :)" else winner) 

	active_char = "X"
	p2_move = False
	board = [[" "," "," "],[" "," "," "],[" "," "," "]]

	new_g = input("wanna play another game? (y/n): ").lower()
	while new_g not in ["y", "n"]:
		new_g = input("wanna play another game? (y/n): ").lower()
	if new_g == "n":
		sys.exit()

	new_p = input("wanna change the players? (y/n): ").lower()
	while new_p not in ["y", "n"]:
		new_p = input("wanna change the players? (y/n): ").lower()
	if new_p == "y":
		p1, p2 = menu()
	return [p1, p2, p2_move, active_char, board]

def main():
	p1, p2 = menu()
	
	board = [[" "," "," "],[" "," "," "],[" "," "," "]]
	active_char = "X"
	p2_move = False

	
	while True:
		print_board(board)
		print("%s's turn" % active_char)

		to_play = p2.get_move(board) if p2_move else p1.get_move(board)
		board[to_play[0]][to_play[1]] = active_char

		p2_move = not p2_move
		active_char = "O" if active_char == "X" else "X"
		
		winner = check_win(board)
		if winner: # game is over
			print_board(board) # show the tha winning move
			p1, p2, p2_move, active_char, board = new_game(board, winner, p1, p2)
			
if __name__ == '__main__':
	main()