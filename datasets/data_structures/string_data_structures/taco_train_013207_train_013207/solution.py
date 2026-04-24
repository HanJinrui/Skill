class Solution:

	def allPairs(self, A, B, N, M, X):
		pairs = [(u, X - u) for u in A if X - u in B]
		pairs.sort()
		return pairs
