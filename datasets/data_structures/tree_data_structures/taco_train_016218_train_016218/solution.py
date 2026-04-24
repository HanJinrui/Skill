class Solution:

	def InOrder(self, root):
		if root == None:
			return []
		return self.InOrder(root.left) + [root.data] + self.InOrder(root.right)
