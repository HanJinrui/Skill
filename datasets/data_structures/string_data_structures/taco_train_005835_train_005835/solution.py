import re

class Solution:

	def search(self, patt, s):
		res = [i + 1 for i in range(len(s)) if s.startswith(patt, i)]
		if len(res) != 0:
			return res
		else:
			return [-1]
