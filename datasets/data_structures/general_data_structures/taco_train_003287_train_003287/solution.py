class Solution:

	def segregateEvenOdd(self, arr, n):
		a = sorted((i for i in arr if i % 2 == 0))
		b = sorted((i for i in arr if i % 2 != 0))
		arr[:] = a + b
		return arr
