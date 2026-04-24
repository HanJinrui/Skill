class Solution:

	def segregateElements(self, arr, n):
		arr[:] = [i for i in arr if i > 0] + [i for i in arr if i < 0]
		return arr
