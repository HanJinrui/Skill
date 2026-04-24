class Solution:

	def findWinner(self, N, X, Y):
		win = [False for _ in range(N + 1)]
		moves = [1, X, Y]
		for i in range(N + 1):
			for move in moves:
				if i - move >= 0 and (not win[i - move]):
					win[i] = True
		return int(win[N])
