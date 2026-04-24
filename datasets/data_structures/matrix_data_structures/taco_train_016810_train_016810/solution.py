class Solution:

	def squaresInMatrix(self, m, n):
		sum = 0
		for i in range(min(m, n)):
			sum += (m - i) * (n - i)
		return sum
