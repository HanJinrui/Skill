class Solution:

	def distinct(self, m, n):
		return len(set(m[0]).intersection(*m))
