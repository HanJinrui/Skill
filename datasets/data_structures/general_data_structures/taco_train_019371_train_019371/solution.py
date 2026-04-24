class Solution:

	def rotateMatrix(self, arr, n):
		l = []
		for i in zip(*arr):
			l = [i] + l
		arr[:] = l[:]
