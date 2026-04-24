class Solution:

	def maxFruits(self, arr, n, m):
		s = 0
		for i in range(m):
			s = s + arr[i]
		a = s
		for i in range(m, m + n):
			s = s + arr[i % n] - arr[(i - m) % n]
			if s > a:
				a = s
		return a
