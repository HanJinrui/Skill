class Solution:

	def findLargest(self, n, s):
		r = 0
		for i in range(1, n + 1):
			if s >= 9:
				r = r * 10 + 9
				s -= 9
			else:
				r = r * 10 + s
				s = 0
		if len(str(r)) < n or s > 0:
			return -1
		return r
