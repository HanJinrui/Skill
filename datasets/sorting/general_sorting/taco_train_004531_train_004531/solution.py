class Solution:

	def max_non_overlapping(self, r):
		r.sort(key=lambda x: x[1])
		a = -1
		c = 0
		for i in r:
			if i[0] >= a:
				a = i[1]
				c += 1
		return c
