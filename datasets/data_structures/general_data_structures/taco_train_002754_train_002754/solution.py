class Solution:

	def unique_substring(self, str):
		x = {}
		for i in range(len(str)):
			for j in range(i + 1, len(str) + 1):
				x[str[i:j]] = 1
		return len(x)
