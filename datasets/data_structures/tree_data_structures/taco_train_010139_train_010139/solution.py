class Solution:

	def imgMultiply(self, root):

		def dfs(l, r):
			if l == None:
				return 0
			elif r == None:
				return 0
			return l.data * r.data + dfs(l.left, r.right) + dfs(l.right, r.left)
		return (root.data ** 2 + dfs(root.left, root.right)) % (10 ** 9 + 7)
