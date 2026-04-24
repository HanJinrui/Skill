class Solution:

	def maxLen(self, n, arr):
		ans = 0
		d = {0: -1}
		Sum = 0
		for i in range(n):
			Sum += arr[i]
			if Sum in d:
				ans = max(ans, i - d[Sum])
			else:
				d[Sum] = i
		return ans
