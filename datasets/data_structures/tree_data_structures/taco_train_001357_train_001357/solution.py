from collections import deque

class Solution:

	def nextRight(self, root, key):
		q = [(root, 0)]
		while q:
			(x, l) = q.pop(0)
			if x.data == key:
				if q and q[0][1] == l:
					return q[0][0]
				return Node(-1)
			if x.left:
				q.append((x.left, l + 1))
			if x.right:
				q.append((x.right, l + 1))
