class Solution:

	def distributeCandy(self, r):
		self.ans = 0

		def ss(node):
			if not node:
				return 0
			l = ss(node.left)
			r = ss(node.right)
			self.ans += abs(l) + abs(r)
			return l + r + node.data - 1
		ss(r)
		return self.ans
