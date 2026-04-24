class Solution:

	def check(self, root):
		s = set()

		def dfs(x, h):
			if x.left:
				dfs(x.left, h + 1)
			if x.right:
				dfs(x.right, h + 1)
			if not x.left and (not x.right):
				s.add(h)
		dfs(root, 0)
		return len(s) == 1
