class MagicDictionary:

	def __init__(self):
		self.hsh = collections.defaultdict(list)

	def buildDict(self, dict):
		for word in dict:
			self.hsh[len(word)].append(word)

	def search(self, word):
		return any((sum((x != y for (x, y) in zip(word, candidate))) == 1 for candidate in self.hsh[len(word)]))
