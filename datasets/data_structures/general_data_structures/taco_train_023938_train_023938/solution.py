class Solution:

	def smallestSubWithSum(self, a, n, x):
		min_l = n
		for i in range(n):
			s = 0
			for j in range(i, n):
				s += a[j]
				if s > x:
					min_l = min(min_l, j - i + 1)
					break
		return min_l
