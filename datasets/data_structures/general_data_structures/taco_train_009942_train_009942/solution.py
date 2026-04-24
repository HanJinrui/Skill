class Solution:

	def kTop(self, a, n, k):
		d = {}
		ans = []
		for i in range(n):
			if a[i] in d:
				d[a[i]] += 1
			else:
				d[a[i]] = 1
			ans += sorted(d.keys(), key=lambda x: (-d[x], x))[:k]
		return ans
