class Solution:

	def CountPairs(self, arr, n):
		p = n - arr.count(1)
		q = arr.count(2)
		res = p * (p - 1) // 2 - q * (q - 1) // 2
		return res
