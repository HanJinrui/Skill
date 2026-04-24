class Solution:

	def isPossible(self, n, m, s):
		x = [0]
		y = [0]
		p = 0
		q = 0
		for i in s:
			if i == 'L':
				q -= 1
			if i == 'R':
				q += 1
			if i == 'U':
				p -= 1
			if i == 'D':
				p += 1
			x.append(p)
			y.append(q)
		if max(x) - min(x) + 1 <= n and max(y) - min(y) + 1 <= m:
			return 1
		return 0
