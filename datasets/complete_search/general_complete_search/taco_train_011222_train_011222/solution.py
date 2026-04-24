class Solution:

	def commonElements(self, a, b, c, n1, n2, n3):
		return sorted(list(set(a) & set(b) & set(c)))
