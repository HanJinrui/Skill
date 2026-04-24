class Solution:

	def countWays(self, n):
		d = [1, 1, 2]
		i = 3
		while i <= n:
			j = sum(d)
			d[i % 3] = j
			i += 1
		return d[n % 3] % (10 ** 9 + 7)
