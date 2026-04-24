class Solution:

	def uniqueNumbers(self, L, R):
		return [i for i in range(L, R + 1) if len(str(i)) == len(set(str(i)))]
