class Solution:

	def orderedPrime(self, n):
		from collections import Counter
		rec = Counter()
		div = 2
		while n > 1:
			if n % div == 0:
				n //= div
				rec[div] += 1
			else:
				div += 1
		res = list(rec.values())
		res.sort()
		ans = 1
		for x in res:
			ans *= x + 1
		res.append(ans)
		return res
