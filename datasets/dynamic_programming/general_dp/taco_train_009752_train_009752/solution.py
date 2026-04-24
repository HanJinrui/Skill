class Solution:

	def minCount(self, arr, n):
		inf = float('inf')
		dic = {}

		def dfs(mn, mx, i):
			if (mn, mx, i + 1) in dic:
				return dic[mn, mx, i + 1]
			if i >= n:
				return 0
			ans = inf
			if arr[i] < mx:
				ans = min(ans, dfs(mn, arr[i], i + 1))
			if arr[i] > mn:
				ans = min(ans, dfs(arr[i], mx, i + 1))
			ans = min(ans, 1 + dfs(mn, mx, i + 1))
			dic[mn, mx, i + 1] = ans
			return ans
		return dfs(-inf, inf, 0)
