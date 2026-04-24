class Solution:

	def isIdentical(self, root1, root2):
		if not root1 or not root2:
			return root1 == root2
		return root1.data == root2.data and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
