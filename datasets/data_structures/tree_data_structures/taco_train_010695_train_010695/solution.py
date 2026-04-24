class Solution:

	def isSymmetric(self, root):

		def isSymmetricc(p, q):
			if not p or not q:
				return p == q
			return p.data == q.data and isSymmetricc(p.left, q.right) and isSymmetricc(p.right, q.left)
		return isSymmetricc(root, root)
