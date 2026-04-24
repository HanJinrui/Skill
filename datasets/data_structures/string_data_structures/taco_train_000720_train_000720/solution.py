from collections import OrderedDict

class LRUCache:

	def __init__(self, cap):
		self.c = OrderedDict()
		self.cap = cap

	def get(self, key):
		if key not in self.c:
			return -1
		else:
			self.c.move_to_end(key)
			return self.c[key]

	def set(self, key, value):
		self.c[key] = value
		self.c.move_to_end(key)
		if len(self.c) > self.cap:
			self.c.popitem(last=False)
