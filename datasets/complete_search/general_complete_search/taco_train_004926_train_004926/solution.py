class Solution:

	def subsetSums(self, arr, N):
		l = [[]]
		for i in arr:
			l += [j + [i] for j in l]
		l = [sum(i) for i in l]
		return l
