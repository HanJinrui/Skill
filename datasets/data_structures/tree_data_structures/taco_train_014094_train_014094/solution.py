class Solution:

	def rightLeafSum(self, root):

		def fun(r, idx):
			if r is None:
				return 0
			if r.left is None and r.right is None:
				if idx == 'r':
					return r.data
				else:
					return 0
			return fun(r.right, 'r') + fun(r.left, 'l')
		return fun(root, '')
