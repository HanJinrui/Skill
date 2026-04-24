class Solution:

	def nextPalin(self, s):
		n = len(s)
		odd = [s[n // 2]] if n % 2 == 1 else []
		s = [i for i in s[:n // 2]]
		size = len(s)
		if size > 1:
			i = size - 2
			while i >= 0 and s[i] >= s[i + 1]:
				i -= 1
			if i == -1:
				return -1
			j = size - 1
			while j >= 0 and s[i] >= s[j]:
				j -= 1
			(s[i], s[j]) = (s[j], s[i])
			s = s[:i + 1] + s[i + 1:][::-1]
			s = s + odd + s[::-1]
			return ''.join(s)
		else:
			return -1
