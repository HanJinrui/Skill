import math

class Solution:

	def minimumSum(self, s: str) -> int:
		l = 0
		h = len(s) - 1
		s = list(s)
		while l < h:
			if s[l] != s[h]:
				if s[l] == '?':
					s[l] = s[h]
				elif s[h] == '?':
					s[h] = s[l]
				else:
					return -1
			l += 1
			h -= 1
		ans = 0
		c = '?'
		for i in range(len(s)):
			if s[i] != '?':
				if c == '?':
					c = s[i]
				else:
					ans += abs(ord(s[i]) - ord(c))
					c = s[i]
		return ans
