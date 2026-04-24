class Solution:

	def maxIntersections(self, lines, N):
		o = {}
		for i in lines:
			o[i[0]] = o.get(i[0], 0) + 1
			o[i[1] + 1] = o.get(i[1] + 1, 0) - 1
		p = 0
		m = 1
		for i in sorted(o):
			p = p + o[i]
			m = max(m, p)
		return m
