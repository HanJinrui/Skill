class Solution:

	def collatzLength(self, N):

		def f(n, memo):
			if n == 1:
				return 1
			if n in memo:
				return memo[n]
			if n % 2 == 0:
				memo[n] = 1 + f(n // 2, memo)
				return memo[n]
			else:
				memo[n] = 1 + f(3 * n + 1, memo)
				return memo[n]
		m = 0
		memo = {}
		for i in range(N, 0, -1):
			m = max(m, f(i, memo))
		return m
