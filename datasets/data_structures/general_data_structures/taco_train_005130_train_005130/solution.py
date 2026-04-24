class Solution:

	def PosNegPair(self, a, n):
		a = list(map(int, a))
		from collections import Counter
		freq = dict(Counter(a))
		all_keys = sorted(list(freq.keys()))
		ans = []
		for i in all_keys:
			if i < 0 and freq.get(-i) != None:
				ans += [-i, i] * min(freq[i], freq[-i])
		return ans[::-1]
