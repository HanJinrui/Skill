class MyStack:

	def __init__(self):
		self.arr = []

	def push(self, data):
		self.arr.append(data)

	def pop(self):
		if len(self.arr) > 0:
			return self.arr.pop()
		return -1
