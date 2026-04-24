class Solution:

	def areMirror(self, a, b):
		if a is None and b is None:
			return True
		if a is None or b is None:
			return False
		return a.data == b.data and self.areMirror(a.left, b.right) and self.areMirror(a.right, b.left)
