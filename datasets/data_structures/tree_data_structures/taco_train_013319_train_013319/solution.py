class Solution:

	def asd(self, x, y, target, a):
		if x == None or y == None:
			return
		else:
			if x.data == target:
				a.append(y.data)
			self.asd(x.left, y.right, target, a)
			self.asd(x.right, y.left, target, a)

	def findMirror(self, root, target):
		a = []
		self.asd(root, root, target, a)
		if a == []:
			return -1
		return a[0]
