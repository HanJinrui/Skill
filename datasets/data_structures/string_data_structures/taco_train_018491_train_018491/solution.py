def insert(root, key):
	for ch in key:
		i = ord(ch) - ord('a')
		if not root.children[i]:
			root.children[i] = TrieNode()
		root = root.children[i]
	root.isEndOfWord = True

def search(root, key):
	for ch in key:
		i = ord(ch) - ord('a')
		if not root.children[i]:
			return False
		root = root.children[i]
	return root.isEndOfWord
