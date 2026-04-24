from collections import deque

class Solution:

	def bottomView(self, root):
		if not root:
			return []
		d = {}
		q = deque([(root, 0)])
		while q:
			(x, l) = q.popleft()
			d[l] = x.data
			if x.left:
				q.append((x.left, l - 1))
			if x.right:
				q.append((x.right, l + 1))
		return [d[x] for x in sorted(d)]
