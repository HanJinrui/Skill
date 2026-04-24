def Moves(N, M, S, pos, board):
	if M == 0:
		return 1
	moves = 0
	for x in range(max(pos[0] - S, 0), min(pos[0] + S + 1, N)):
		for y in range(max(pos[1] - S + abs(x - pos[0]), 0), min(pos[1] + S - abs(x - pos[0]) + 1, N)):
			if board[x][y] != 'P':
				moves += Moves(N, M - 1, S, (x, y), board)
	return moves

def DoTest():
	(N, M, S) = input().split(' ')
	N = int(N)
	M = int(M)
	S = int(S)
	pos = (-2, -2)
	board = []
	for x in range(0, N):
		row = input()
		if 'L' in row:
			pos = (x, row.find('L'))
		board.append(row)
	print(Moves(N, M, S, pos, board))
T = int(input())
for test in range(0, T):
	DoTest()
