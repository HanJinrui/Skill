class Solution:

	def kSmallestElements(self, a, n, k):
		d = {}
		for i in range(n):
			d[i] = arr[i]
		result = sorted(d.items(), key=lambda x: x[1])[:k]
		return [item[1] for item in sorted(result)]
