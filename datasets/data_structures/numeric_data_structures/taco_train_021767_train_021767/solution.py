class Solution:

	def countEvenSum(self, arr, n):
		s = 0
		res = 0
		for i in range(n - 1, -1, -1):
			if arr[i] & 1:
				s = n - i - 1 - s
			else:
				s = s + 1
			res = res + s
		return res
