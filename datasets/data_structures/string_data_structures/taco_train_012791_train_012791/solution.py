class Solution:

	def deleteKey(self, root, key):
		for c in key:
			idx = ord(c) - 97
			root = root.children[idx]
		root.isEndOfWord = False
