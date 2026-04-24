class Solution:

	def getMaxSum(self, root):

		def maxsum(root):
			if root == None:
				return [0, 0]
			x = maxsum(root.left)
			y = maxsum(root.right)
			return [root.data + x[1] + y[1], max(x) + max(y)]
		return max(maxsum(root))
