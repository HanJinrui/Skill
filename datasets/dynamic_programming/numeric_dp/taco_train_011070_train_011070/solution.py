class Solution:

	def TotalWays(self, N):
		a = [0, 1]
		for i in range(N + 3):
			a.append(a[i] + a[i + 1])
		return a[N + 2] * a[N + 2] % 1000000007
