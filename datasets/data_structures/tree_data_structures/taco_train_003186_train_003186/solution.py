class Solution:

	def levelOrder(self, root):
		a = [root]
		res = []
		while len(a) > 0:
			p = a.pop(0)
			if p.left:
				a.append(p.left)
			if p.right:
				a.append(p.right)
			res.append(p.data)
		return res
