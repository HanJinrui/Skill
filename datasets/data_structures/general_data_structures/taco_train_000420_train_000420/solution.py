class stack:

	def __init__(self):
		self.s = []

	def push(self, x):
		self.s.append(x)

	def pop(self):
		if self.s:
			k = self.s.pop(-1)
		else:
			k = -1
		return k

	def getMin(self):
		if not self.s:
			return -1
		return min(self.s)
