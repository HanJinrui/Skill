class Solution:

	def isIdealPermutation(self, A):
		return all((abs(v - i) <= 1 for (i, v) in enumerate(A)))
