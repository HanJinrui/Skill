class MyStack:

	def __init__(self):
		self.s = []

	def push(self, data):
		self.s.append(data)

	def pop(self):
		if len(self.s) == 0:
			return -1
		return self.s.pop()
