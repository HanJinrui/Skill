class Solution:

	def printAllDups(self, root):
		d = {}
		res = []

		def fun(root):
			if root == None:
				return 'N'
			s = ','.join([str(root.data), fun(root.left), fun(root.right)])
			if s in d:
				d[s] = d[s] + 1
				if d[s] == 2:
					res.append(root)
			else:
				d[s] = 1
			return s
		fun(root)
		res.sort(key=lambda x: x.data)
		return res
