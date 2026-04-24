class Solution:

	def search(self, a: list, l: int, h: int, key: int):
		if key in a:
			return a.index(key)
		return -1
