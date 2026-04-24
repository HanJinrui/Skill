class Solution:

	def Ancestors(self, root, target):
		res = []

		def helper(root):
			if not root:
				return False
			if root.data == target:
				return True
			if helper(root.left) or helper(root.right):
				res.append(root.data)
				return True
		helper(root)
		return res
