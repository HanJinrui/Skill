class Solution:

	def mirror(self, root):
		if root:
			(root.left, root.right) = (root.right, root.left)
			self.mirror(root.left)
			self.mirror(root.right)
