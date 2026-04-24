class Solution:

	def preOrder(self, root):
		a = []

		def rec(root):
			if root:
				a.append(root.data)
				rec(root.left)
				rec(root.right)
		rec(root)
		return a
