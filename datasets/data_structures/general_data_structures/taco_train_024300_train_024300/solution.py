class Queue:

	def __init__(self):
		self.s1 = []

	def enqueue(self, X):
		self.s1.append(X)

	def dequeue(self):
		return self.s1.pop(0)
