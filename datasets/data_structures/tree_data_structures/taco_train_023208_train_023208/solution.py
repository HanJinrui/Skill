class Solution:

	def minDepth(self, root):
		if root == None:
			return 0
		a = self.minDepth(root.left)
		b = self.minDepth(root.right)
		if a == 0 or b == 0:
			return max(a, b) + 1
		else:
			return min(a, b) + 1
