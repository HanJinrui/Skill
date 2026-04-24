class Solution:

	def populateNext(self, root):

		def solve(node, prev):
			if not node:
				return
			solve(node.left, prev)
			if prev[0]:
				prev[0].next = node
			prev[0] = node
			solve(node.right, prev)
		prev = [None]
		solve(root, prev)
