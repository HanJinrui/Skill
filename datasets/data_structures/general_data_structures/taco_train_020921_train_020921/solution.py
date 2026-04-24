class Solution:

	def solve(self, arr, n, k):
		arr.sort()
		summa = sum(arr)
		return max(abs(summa - 2 * sum(arr[:k])), abs(summa - 2 * sum(arr[-k:])))
