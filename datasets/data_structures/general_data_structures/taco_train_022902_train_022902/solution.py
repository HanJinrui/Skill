class Solution:

	def maximizeSum(self, arr, n):
		a = [0] * (max(arr) + 1)
		ans = 0
		for r in arr:
			a[r] += 1
		for i in range(max(arr), 0, -1):
			if a[i] > 0:
				ans += i * a[i]
				a[i - 1] -= a[i]
		return ans
