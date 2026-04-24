class Solution:
	ans = True

	def get_height(self, node):
		if node is None:
			return 0
		lh = self.get_height(node.left)
		rh = self.get_height(node.right)
		if lh != rh:
			self.ans = False
		return max(lh, rh) + 1

	def isPerfect(self, root):
		self.get_height(root)
		return self.ans
