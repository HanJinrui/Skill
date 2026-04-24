class Solution:

	def getCount(self, root, n):
		q = [root]
		lev = 0
		m = 0
		while q:
			l = len(q)
			lev += 1
			for i in range(l):
				p = q.pop(0)
				if p.left is None and p.right is None and (n >= lev):
					m += 1
					n -= lev
				if p.left:
					q.append(p.left)
				if p.right:
					q.append(p.right)
		return m
