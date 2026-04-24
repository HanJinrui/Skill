class Solution:

	def transpose(self, matrix, n):
		lst = []
		for i in zip(*matrix):
			lst += [i]
		matrix[:] = lst[:]
