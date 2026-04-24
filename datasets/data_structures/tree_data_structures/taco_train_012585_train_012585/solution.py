class Solution:

	def rightView(self, root):
		arr = []

		def left(node, depth):
			if not node:
				return
			if depth == len(arr):
				arr.append(node.data)
			left(node.right, depth + 1)
			left(node.left, depth + 1)
		left(root, 0)
		return arr
