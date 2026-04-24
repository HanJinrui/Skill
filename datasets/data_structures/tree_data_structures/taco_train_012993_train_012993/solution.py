class Solution:

	def depthOfOddLeaf(self, root):

		def calculate(root, level):
			if root == None:
				return 0
			elif root.left == None and root.right == None and level & 1:
				return level
			else:
				return max(calculate(root.left, level + 1), calculate(root.right, level + 1))
		return calculate(root, 1)
