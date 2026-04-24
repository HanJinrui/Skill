class Solution:

	def findMaxAverage(self, a, n, k):
		idx = 0
		s = sum(a[:k])
		ans = s
		for i in range(k, n):
			s += a[i] - a[i - k]
			if s > ans:
				ans = s
				idx = i - k + 1
		return idx
