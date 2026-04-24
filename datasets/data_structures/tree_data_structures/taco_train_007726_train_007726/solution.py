class Solution:
	h = None
	p = None

	def bToDLL(self, r):
		if not r:
			return
		self.bToDLL(r.left)
		if self.p == None:
			self.h = r
		else:
			self.p.right = r
			r.left = self.p
		self.p = r
		self.bToDLL(r.right)
		return self.h
