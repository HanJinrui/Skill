class Solution:

	def numberWithNoConsecutiveOnes(self, n):
		l = []
		for i in range(1, 2 ** n):
			if i & i << 1 == 0:
				l.append(i)
		return l
