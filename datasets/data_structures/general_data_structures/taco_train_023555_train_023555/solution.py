class Solution:

	def minMoves(self, arr, n):
		e = n
		for ele in reversed(arr):
			if ele == e:
				e -= 1
		return e
