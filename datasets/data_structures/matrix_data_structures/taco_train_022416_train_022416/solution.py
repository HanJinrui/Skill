class Solution:

	def firstElement(self, n):
		m = 1000000007
		a = 0
		b = 1
		for _ in range(n):
			(a, b) = (b, (a + b) % m)
		return a
