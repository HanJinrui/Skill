class Solution:

	def postOrder(self, root):
		a = []

		def rec(root):
			if root:
				rec(root.left)
				rec(root.right)
				a.append(root.data)
		rec(root)
		return a
