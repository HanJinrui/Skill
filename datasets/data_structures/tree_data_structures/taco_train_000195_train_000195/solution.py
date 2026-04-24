from queue import Queue

class Solution:

	def diagonal(self, root):
		q = [root]
		while q:
			x = q.pop(0)
			while x:
				print(x.data, end=' ')
				if x.left:
					q.append(x.left)
				x = x.right
		return []
