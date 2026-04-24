class Solution:

	def minValue(self, s, k):
		d = {}
		for i in s:
			if i not in d:
				d[i] = 0
			d[i] += 1
		l = list(d.values())
		while k:
			i = l.index(max(l))
			l[i] -= 1
			k -= 1
		return sum([i ** 2 for i in l])
