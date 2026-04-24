class Solution:

	def lca(self, root, n1, n2):
		if root == None or root.data == n1 or root.data == n2:
			return root
		l = self.lca(root.left, n1, n2)
		r = self.lca(root.right, n1, n2)
		if l == None:
			return r
		elif r == None:
			return l
		else:
			return root
