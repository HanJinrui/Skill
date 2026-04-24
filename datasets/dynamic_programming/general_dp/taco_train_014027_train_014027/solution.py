class Solution:

	def prefixStrings(self, N):
		cat = 1
		for i in range(1, N + 1):
			cat *= 4 * i - 2
			cat //= i + 1
		return cat % (10 ** 9 + 7)
