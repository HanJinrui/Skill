class Solution:

	def minTime(self, s1, s2, n):
		t = 1 + (s1 * s2 * n - 1) // (s1 + s2)
		if t // s1 + t // s2 < n:
			return t + min(s1 - t % s1, s2 - t % s2)
		return t
