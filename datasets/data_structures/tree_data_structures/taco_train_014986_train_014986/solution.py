class Solution:

	def countNonLeafNodes(self, root):
		if root == None or root.left == root.right:
			return 0
		else:
			return 1 + self.countNonLeafNodes(root.left) + self.countNonLeafNodes(root.right)
