class Solution:

	def find(self, root, val, f):
		if root:
			if f and val == 0:
				self.ans += root.data
			if root.data == target:
				self.f = 1
				self.find(root.left, -1, 1)
				self.find(root.right, 1, 1)
			else:
				self.find(root.left, val - 1, f)
				self.find(root.right, val + 1, f)

	def verticallyDownBST(self, root, target):
		self.ans = 0
		self.f = 0
		self.find(root, 0, 0)
		if not self.f:
			return -1
		return self.ans
