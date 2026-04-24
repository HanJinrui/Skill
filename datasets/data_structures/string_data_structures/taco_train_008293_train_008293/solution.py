class Solution:

	def subArraySum(self, arr, n, sum):
		d = {0: 1}
		s = 0
		r = 0
		for x in arr:
			s += x
			if s - sum in d:
				r += d[s - sum]
			d[s] = d.setdefault(s, 0) + 1
		return r
