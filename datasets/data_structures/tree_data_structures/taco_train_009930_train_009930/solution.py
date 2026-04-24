from math import gcd

class Solution:

	def maxGCD(self, root):
		return self.gcd(root)[1]

	def gcd(self, node):
		if node is None:
			return (0, 0)
		a = (0, 0)
		if node.left and node.right:
			a = (gcd(node.left.data, node.right.data), node.data)
		b = self.gcd(node.left)
		c = self.gcd(node.right)
		return max(a, b, c)
