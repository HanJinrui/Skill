class Solution:

	def search(self, A, N):
		x = 0
		for i in A:
			x ^= i
		return x
