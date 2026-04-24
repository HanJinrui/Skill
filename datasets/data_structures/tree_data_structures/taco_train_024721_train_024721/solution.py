class Solution:
	prev = None

	def flatten(self, root):
		if root == None:
			return
		self.flatten(root.right)
		self.flatten(root.left)
		root.right = self.prev
		root.left = None
		self.prev = root
