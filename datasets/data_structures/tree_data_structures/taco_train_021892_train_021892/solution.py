class Solution:

	def tiltTree(self, root):
		self.s = 0

		def help(root):
			if not root:
				return 0
			l = help(root.left)
			r = help(root.right)
			self.s += abs(r - l)
			return l + root.data + r
		help(root)
		return self.s
