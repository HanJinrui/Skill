class Solution:

	def sortedCount(self, N, M, Mat):
		c = 0
		for i in Mat:
			t = sorted(list(set(i)))
			if i == t or i == t[::-1]:
				c += 1
		return c
