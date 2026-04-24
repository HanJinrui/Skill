class Solution:

	def getMaxandMinProduct(self, arr, n):
		x = [1, 1]
		while sum(x[-2:]) <= max(arr):
			x.append(sum(x[-2:]))
		return [i for i in arr if i in x]
