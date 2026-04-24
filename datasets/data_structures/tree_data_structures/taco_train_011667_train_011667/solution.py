import sys
sys.setrecursionlimit(150000)

class Node:

	def __init__(self, val):
		self.right = None
		self.data = val
		self.left = None

class Solution:

	def maxDepth(self, root):
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
