import math

def raj(a, b):
	p = math.factorial(a) // (math.factorial(b) * math.factorial(a - b))
	return p % 1000000007

class Solution:

	def countWays(self, m, n, p, arr):
		if m - p < sum(arr):
			return -1
		m = m - p
		if m == sum(arr):
			return 1
		else:
			d = m - sum(arr) + n - 1
			c = n - 1
			return raj(d, c)
