class Solution:

	def getMaxWidth(self, root):
		q = [root]
		res = 0
		while q:
			l = len(q)
			res = max(res, l)
			for i in range(l):
				p = q.pop(0)
				if p.left:
					q.append(p.left)
				if p.right:
					q.append(p.right)
		return res
