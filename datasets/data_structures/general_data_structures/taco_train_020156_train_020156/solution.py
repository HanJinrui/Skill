class MyQueue:

	def __init__(self):
		self.q1 = []

	def push(self, item):
		self.q1.append(item)

	def pop(self):
		if len(self.q1) == 0:
			return -1
		x = self.q1.pop(0)
		return x
