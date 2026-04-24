class Solution:

	def btWithKleaves(self, root, k):

		def _solve(nd):
			if not nd:
				return 0
			L = _solve(nd.left)
			R = _solve(nd.right)
			V = L + R
			if V > 0 and V == k:
				ans.append(nd.data)
			return V if V > 0 else 1
		ans = []
		_solve(root)
		return ans if ans else [-1]
