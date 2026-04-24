class Solution:

	def leftSmaller(self, n, a):
		ans = [-1] * n
		for i in range(1, n):
			for j in range(i - 1, -1, -1):
				if a[j] < a[i]:
					ans[i] = a[j]
					break
		return ans
