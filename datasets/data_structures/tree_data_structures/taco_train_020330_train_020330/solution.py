class Node:

	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

class Solution:

	def helper(self, pre, l, r):
		mid = (l + r) // 2
		node = Node(pre[l])
		if l < r:
			node.left = self.helper(pre, l + 1, mid)
			node.right = self.helper(pre, mid + 1, r)
		return node

	def constructBinaryTree(self, pre, preMirror, size):
		root = self.helper(pre, 0, size - 1)
		return root
