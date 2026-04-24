class Solution:

	def minOperations(self, s1, s2):
		(m, n) = (len(s1), len(s2))
		import functools

		@functools.lru_cache(None)
		def solve(m, n):
			if m == 0:
				return n
			if n == 0:
				return m
			if s1[m - 1] == s2[n - 1]:
				return solve(m - 1, n - 1)
			return min(solve(m, n - 1), solve(m - 1, n)) + 1
		return solve(m, n)
