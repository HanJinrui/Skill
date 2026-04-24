class Solution:

	def scores(self, a, b, cc):
		for (i, j) in zip(a, b):
			if i > j:
				cc[0] += 1
			elif i < j:
				cc[1] += 1
