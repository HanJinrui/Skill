class Solution:

	def countWays(self, n):
		m = 1000000007
		t = [0] * (n + 1)
		t[0] = 1
		for i in range(1, n):
			for j in range(i, n + 1):
				t[j] = (t[j] % m + t[j - i] % m) % m
		return t[n] % m
