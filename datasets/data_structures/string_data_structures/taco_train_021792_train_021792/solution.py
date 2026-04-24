class Solution:

	def prevPermutation(self, s):
		s = list(s)
		i = len(s) - 1
		while i > 0 and s[i - 1] <= s[i]:
			i -= 1
		if i == 0:
			return None
		index = i - 1
		i = len(s) - 1
		while s[i] >= s[index]:
			i -= 1
		(s[i], s[index]) = (s[index], s[i])
		s = s[:index + 1] + s[index + 1:][::-1]
		s = ''.join(s)
		return s
