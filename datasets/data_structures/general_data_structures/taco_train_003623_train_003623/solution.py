class Solution:

	def IsPerfect(self, arr, n):
		return arr == arr[::-1]
