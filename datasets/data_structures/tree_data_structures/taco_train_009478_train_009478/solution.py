class Solution:

	def isSumProperty(self, root):
		res = [1]
		self.helper(root, res)
		return res[0]

	def helper(self, root, res):
		if not root:
			return 0
		l = self.helper(root.left, res)
		r = self.helper(root.right, res)
		if l + r != 0 and l + r != root.data:
			res[0] = 0
		return root.data
