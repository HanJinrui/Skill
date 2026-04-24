class Solution:

	def ExtremeNodes(self, root):
		a = []
		cl = -1
		q = [(root, 0)]
		while q:
			(c, l) = q.pop(0)
			if l % 2 and l > cl or (l % 2 == 0 and (not q or q[0][1] > l)):
				a.append(c.data)
			if l > cl:
				cl = l
			for b in (c.left, c.right):
				if b:
					q.append((b, l + 1))
		return a
