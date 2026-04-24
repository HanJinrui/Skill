import math

class Solution:

	def minimumDays(self, S, N, M):
		p = S // 7
		if N * (S - p) < S * M:
			return -1
		return math.ceil(S * M / N)
