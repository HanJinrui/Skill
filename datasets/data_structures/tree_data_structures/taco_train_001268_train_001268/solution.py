class Solution:

	def isSubTree(self, T, S):
		return self.inOrder(S) in self.inOrder(T)

	def inOrder(self, root):
		if not root:
			return '/'
		return '^' + str(root.data) + '#' + self.inOrder(root.left) + self.inOrder(root.right)
