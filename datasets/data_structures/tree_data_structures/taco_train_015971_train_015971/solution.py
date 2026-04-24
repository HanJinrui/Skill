class Solution:

	def fun(self, root, l):
		if root == None:
			return 0
		le = self.fun(root.left, l)
		re = self.fun(root.right, l)
		if le == 0 and re == 0:
			l.append(root)
			if len(l) % 2 == 0:
				t1 = l[-2].data
				l[-2].data = l[-1].data
				l[-1].data = t1

	def pairwiseSwap(self, root):
		l = []
		self.fun(root, l)
