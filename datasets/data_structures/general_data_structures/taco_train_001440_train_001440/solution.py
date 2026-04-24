import math as m

class Solution:

	def countCoPrime(self, arr, n):
		c = 0
		for i in range(n - 1):
			if m.gcd(arr[i], arr[i + 1]) != 1:
				c = c + 1
		return c
