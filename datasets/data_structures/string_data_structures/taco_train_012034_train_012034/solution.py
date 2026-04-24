import heapq
from collections import Counter

class Solution:

	def rearrangeString(self, str):
		res = ''
		z = []
		c = Counter(str)
		for (i, j) in c.items():
			heapq.heappush(z, (-j, i))
		p = [1, '']
		while z:
			(i, j) = heapq.heappop(z)
			res += j
			if -p[0] > 0:
				heapq.heappush(z, (p[0], p[1]))
			i += 1
			p = [i, j]
		if len(res) == len(str):
			return res
		else:
			return '-1'
