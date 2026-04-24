from itertools import accumulate

class Solution:

	def solve(self, N, K, arr):
		(S, factors) = (sum(arr), set())
		for i in range(1, int(S ** 0.5) + 1):
			if S % i == 0:
				factors.add(i)
				factors.add(S // i)
		factors = sorted(factors, reverse=True)
		prefixsum = list(accumulate(arr))
		for i in factors:
			count = 0
			for j in prefixsum:
				count += not j % i
				if count >= K:
					return i
