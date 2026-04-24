class Solution:

	def height(self, root):
		if root is None:
			return 0
		return 1 + max(self.height(root.left), self.height(root.right))
