class Solution:

	def numberOfways(self, a, n):
		c = 1
		ans = 1
		for i in range(1, n):
			if arr[i - 1] == arr[i]:
				c += 1
				ans += c
			else:
				ans += 1
				c = 1
		return ans
