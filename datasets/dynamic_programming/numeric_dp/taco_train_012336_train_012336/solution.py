ub = int(100000.0)
sieve = [1] * (ub + 1)
sieve[0] = sieve[1] = -1
for i in range(2, int(ub ** 0.5) + 1):
	if sieve[i]:
		for j in range(i * i, ub + 1, i):
			sieve[j] = 0

class Solution:

	def Count(self, L, R):
		x = sieve[L:R + 1]
		return x.count(0) - x.count(1)
