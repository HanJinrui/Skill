class Solution:

	def findOnce(self, arr: list, n: int):
		c = 2 * sum(set(arr)) - sum(arr)
		return c
