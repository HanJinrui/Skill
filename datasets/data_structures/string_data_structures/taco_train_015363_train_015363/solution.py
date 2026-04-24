from typing import List

class Solution:

	def makePalindrome(self, n: int, arr: List[str]) -> bool:
		d = {}
		for i in arr:
			s = i[::-1]
			if s in d:
				del d[s]
			else:
				d[i] = 1
		if len(d) > 1:
			return False
		else:
			for i in d:
				a = i[::-1]
				if i != a:
					return False
		return True
