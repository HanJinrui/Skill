class Solution:

	def minDist(self, arr, n, x, y):
		(p, ans) = (-1, float('inf'))
		for (i, num) in enumerate(arr):
			if num == x or num == y:
				if p != -1 and num != arr[p]:
					ans = min(ans, i - p)
				p = i
		if ans == float('inf'):
			return -1
		return ans
