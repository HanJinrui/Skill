class MyQueue:

	def __init__(self):
		self.l = []

	def push(self, x):
		self.l.append(x)

	def pop(self):
		return self.l.pop(0) if self.l else -1
