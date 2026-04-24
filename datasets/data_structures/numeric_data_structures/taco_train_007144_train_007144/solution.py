import math

class Solution:

	def countMinOperations(self, arr, n):
		res = 0
		for a in arr:
			res += bin(a)[2:].count('1')
		res += int(math.log(max(arr), 2))
		return res
