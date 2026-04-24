class Solution:

	def minLeafSum(self, root):
		Q = [(root, 0)]
		m = -1
		s = 0
		while Q:
			(r, l) = Q.pop(0)
			if r.left or r.right:
				if r.left:
					Q.append((r.left, l + 1))
				if r.right:
					Q.append((r.right, l + 1))
			elif m == -1 or l == m:
				s += r.data
				m = l
			else:
				break
		return s
