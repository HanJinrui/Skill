class Solution:

	def getLevel(self, root, target):

		def rec(root, lvl):
			if not root:
				return 0
			if root.data == target:
				return lvl
			return rec(root.left, lvl + 1) or rec(root.right, lvl + 1)
		return rec(root, 1)
