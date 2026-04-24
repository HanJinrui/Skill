def load_board(N):
	board = [None] * N
	for i in range(N):
		board[i] = input()
	return board

def is_chef_winner(board, K):
	N = len(board)
	for row in range(N):
		for col in range(N):
			if board[row][col] == '.':
				h_num_X = 1
				i = col - 1
				while i >= 0 and board[row][i] == 'X':
					h_num_X += 1
					i -= 1
				i = col + 1
				while i < N and board[row][i] == 'X':
					h_num_X += 1
					i += 1
				v_num_X = 1
				i = row - 1
				while i >= 0 and board[i][col] == 'X':
					v_num_X += 1
					i -= 1
				i = row + 1
				while i < N and board[i][col] == 'X':
					v_num_X += 1
					i += 1
				d_num_X = 1
				i = row - 1
				j = col - 1
				while i >= 0 and j >= 0 and (board[i][j] == 'X'):
					d_num_X += 1
					i -= 1
					j -= 1
				i = row + 1
				j = col + 1
				while i < N and j < N and (board[i][j] == 'X'):
					d_num_X += 1
					i += 1
					j += 1
				ad_num_X = 1
				i = row - 1
				j = col + 1
				while i >= 0 and j < N and (board[i][j] == 'X'):
					ad_num_X += 1
					i -= 1
					j += 1
				i = row + 1
				j = col - 1
				while i < N and j >= 0 and (board[i][j] == 'X'):
					ad_num_X += 1
					i += 1
					j -= 1
				if h_num_X >= K or v_num_X >= K or d_num_X >= K or (ad_num_X >= K):
					return True
	return False
T = int(input())
for i in range(T):
	(N, K) = map(int, input().split())
	board = load_board(N)
	if is_chef_winner(board, K):
		print('YES')
	else:
		print('NO')
