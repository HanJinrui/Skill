class Solution:

	def nodesAtOddLevels(self, root):
		if node is None:
			return
		if k == 0:
			print(node.data)
			k = l
			return
		else:
			odd_level(node.left, k - 1, l)
			odd_level(node.right, k - 1, l)
