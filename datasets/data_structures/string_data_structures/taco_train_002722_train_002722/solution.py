class Solution:

	def minChar(self, s):
		ans = 0
		i = 0
		j = len(s) - 1
		while i < j:
			if s[i] == s[j]:
				i += 1
			else:
				ans += 1
				if i != 0:
					j += 1
					i -= 1
			j -= 1
		return ans
