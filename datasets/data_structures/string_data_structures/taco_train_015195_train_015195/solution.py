class Solution:

	def search(self, X, Y):
		if Y not in X:
			return -1
		return X.rindex(Y) + 1
