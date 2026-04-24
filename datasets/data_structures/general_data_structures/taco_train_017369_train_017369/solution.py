class Solution:

	def MaxNumber(self, arr, n):
		return ''.join(map(str, sorted(arr, reverse=True)))
