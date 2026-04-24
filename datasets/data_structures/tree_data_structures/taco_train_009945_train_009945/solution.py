class Solution:

	def connect(self, root):
		q = [root]
		while q:
			node = None
			for i in range(len(q)):
				curr = q.pop(0)
				if curr.right:
					q.append(curr.right)
				if curr.left:
					q.append(curr.left)
				curr.nextRight = node
				node = curr
