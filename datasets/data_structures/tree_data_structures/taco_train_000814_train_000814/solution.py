class Solution:

	def hasPathSum(self, root, S):
		if root == None:
			return 0
		if S == root.data and root.left == None and (root.right == None):
			return 1
		return self.hasPathSum(root.left, S - root.data) or self.hasPathSum(root.right, S - root.data)
