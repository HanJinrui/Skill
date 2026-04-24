class Solution:

	def pattern(self, a, N):
		for i in range(N):
			if a[i] == a[i][::-1]:
				return str(i) + ' R'
		for (i, col) in enumerate(zip(*a)):
			if col == col[::-1]:
				return str(i) + ' C'
		return '-1'
