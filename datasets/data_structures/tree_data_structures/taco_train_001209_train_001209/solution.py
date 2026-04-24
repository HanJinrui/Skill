class Solution:

	def maxPathSum(self, root):
		mx = float('-inf')

		def maxsum(r):
			nonlocal mx
			if not r:
				return float('-inf')
			if not r.left and (not r.right):
				return r.data
			l = maxsum(r.left)
			ri = maxsum(r.right)
			mx = max(mx, l + ri + r.data)
			return r.data + max(l, ri)
		y = maxsum(root)
		if not root.left or not root.right:
			return max(y, mx)
		return mx
