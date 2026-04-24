class Solution:

	def isSumTree(self, root):
		if root.left is None and root.right is None:
			return True
		x = 0
		if root.left:
			self.isSumTree(root.left)
			x += root.left.data
		if root.right:
			self.isSumTree(root.right)
			x += root.right.data
		if x == root.data:
			root.data *= 2
			return True
		else:
			return False
