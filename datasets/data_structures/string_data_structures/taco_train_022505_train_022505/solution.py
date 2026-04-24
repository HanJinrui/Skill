class Solution:

	def EvenOdd(self, n1, n2):
		return int(not int(n1) * int(n2) % 2)
