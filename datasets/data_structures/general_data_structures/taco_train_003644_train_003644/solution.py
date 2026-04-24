class Solution:

	def findSubarray(self, a, n):
		d = {}
		i = 0
		j = 0
		while j < n:
			while j < n and a[j] >= 0:
				j += 1
			summa = sum(a[i:j])
			if not summa in d or j - i > len(d[summa]):
				d[summa] = a[i:j]
			while j < n and a[j] < 0:
				j += 1
			i = j
		return d[max(d.keys())]
