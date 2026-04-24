class Solution:

	def printPaths(self, root, sum):
		ans = []

		def walk(n, c, s):
			nonlocal sum
			if not n:
				return
			c.append(n.data)
			s += n.data
			if s == sum:
				ans.append(c[:])
			walk(n.left, c[:], s)
			walk(n.right, c, s)
		walk(root, [], 0)
		return ans
