class RandomizedSet:

	def __init__(self):
		self.dic = {}
		self.l = []

	def insert(self, val):
		if val in self.dic:
			return False
		self.l.append(val)
		self.dic[val] = len(self.l) - 1
		return True

	def remove(self, val):
		if val not in self.dic:
			return False
		self.dic[self.l[-1]] = self.dic[val]
		(self.l[self.dic[val]], self.l[-1]) = (self.l[-1], self.l[self.dic[val]])
		self.l.pop()
		del self.dic[val]
		return True

	def getRandom(self):
		return random.choice(self.l)
