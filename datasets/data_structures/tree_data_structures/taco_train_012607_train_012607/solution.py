class Solution:

	def dupSub(self, root):
		d = {}
		res = [0]

		def fun(root):
			if root == None:
				return 'N'
			if root.left == None and root.right == None:
				s = str(root.data)
				return s
			s = ','.join([str(root.data), fun(root.left), fun(root.right)])
			if s in d:
				res[0] = 1
			else:
				d[s] = 1
			return s
		fun(root)
		return res[0]
