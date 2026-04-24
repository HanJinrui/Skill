class Solution:

	def countElements(self, N, A):
		X = list(set(A))
		return max(X) - min(X) - len(X) + 1
