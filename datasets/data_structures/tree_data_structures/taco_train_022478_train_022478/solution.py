class Solution:

	def findDist(self, root, a, b):
		(x, y) = ([], [])

		def manu(root, ans, p):
			if root is None:
				return False
			ans.append(root.data)
			if root.data == p:
				return True
			if manu(root.left, ans, p) or manu(root.right, ans, p):
				return True
			ans.pop()
			return
		manu(root, x, a)
		manu(root, y, b)
		i = 0
		k = min(len(x), len(y))
		while i < k - 1:
			if x[0] == y[0] and x[1] == y[1]:
				x.pop(0)
				y.pop(0)
			else:
				break
			i += 1
		return len(x) + len(y) - 2
