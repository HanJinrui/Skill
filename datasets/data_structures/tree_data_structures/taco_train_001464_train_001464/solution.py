class Solution:

	def getLevelDiff(self, root):
		if root is None:
			return 0
		return root.data - self.getLevelDiff(root.left) - self.getLevelDiff(root.right)
