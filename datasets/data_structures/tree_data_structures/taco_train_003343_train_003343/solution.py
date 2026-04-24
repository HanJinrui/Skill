class Solution:

	def isBalanced(self, root):
		if root == None:
			return 1
		lh = self.isBalanced(root.left)
		if lh == 0:
			return 0
		rh = self.isBalanced(root.right)
		if rh == 0:
			return 0
		if abs(lh - rh) > 1:
			return 0
		return max(lh, rh) + 1
