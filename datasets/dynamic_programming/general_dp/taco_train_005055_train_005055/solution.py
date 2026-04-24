def jump(i, j):
	if i < 0 or j < 0 or i >= n or (j >= n):
		return 0
	if dp[i][j] != -1:
		return dp[i][j]
	dp[i][j] = 1 if board[i][j] == 'P' else 0
	dp[i][j] += max(jump(i - 1, j + 2), jump(i - 2, j + 1), jump(i + 1, j + 2), jump(i + 2, j + 1))
	return dp[i][j]
t = int(input())
for _ in range(t):
	n = int(input())
	board = [['.' for _ in range(n)] for _ in range(n)]
	for i in range(n):
		board[i] = list(input())
		if 'K' in board[i]:
			loc_k = (i, board[i].index('K'))
	dp = [[-1 for _ in range(n)] for _ in range(n)]
	print(jump(loc_k[0], loc_k[1]))
