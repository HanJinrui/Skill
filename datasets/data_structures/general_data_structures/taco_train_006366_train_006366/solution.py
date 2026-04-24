from collections import defaultdict

class Solution:

	def longLenSub(self, arr, n):
		mx = 0
		d = defaultdict(int)
		for ele in arr:
			d[ele] = 1 + max(d[ele - 1], d[ele + 1])
			mx = max(mx, d[ele])
		return mx
