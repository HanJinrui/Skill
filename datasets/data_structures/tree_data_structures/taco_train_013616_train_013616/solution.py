class Solution:

	def toSumTree(self, root):
		if root == None:
			return 0
		ov = root.data
		root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
		return root.data + ov
