class Solution:

	def getSingle(self, arr, n):
		ans = 0
		for x in arr:
			ans ^= x
		return ans
