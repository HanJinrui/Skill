class Solution:

	def isLuckyOrNot(self, N):
		if N < 10:
			return 1
		N = sorted(str(N))
		for j in range(0, len(N) - 1):
			if N[j] == N[j + 1] or N[j] == '1':
				return 0
		return 1
