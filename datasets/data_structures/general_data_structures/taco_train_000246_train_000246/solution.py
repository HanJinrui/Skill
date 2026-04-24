class Solution:

	def isValid(self, board):
		xc = board.count('X')
		oc = board.count('O')
		if xc - oc != 1:
			return False
		win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
		ow = False
		xw = False
		for i in range(8):
			if board[win[i][0]] == 'O' and board[win[i][1]] == 'O' and (board[win[i][2]] == 'O'):
				ow = True
			if board[win[i][0]] == 'X' and board[win[i][1]] == 'X' and (board[win[i][2]] == 'X'):
				xw = True
		if ow:
			return False
		return True
