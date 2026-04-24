class Solution:

	def inOrder(self, root):
		if root is None:
			return []
		return self.inOrder(root.left) + [root.data] + self.inOrder(root.right)
