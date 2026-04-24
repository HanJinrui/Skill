class Solution:

	def EqualSum(self, a, n):
		summa = sum(a)
		diff = float('inf')
		index = 0
		pos = 1
		for (i, item) in enumerate(a):
			summa -= item * 2
			if abs(summa) < diff:
				diff = abs(summa)
				index = i + 2
				if summa >= 0:
					pos = 1
				else:
					pos = 2
		return (diff, index, pos)
