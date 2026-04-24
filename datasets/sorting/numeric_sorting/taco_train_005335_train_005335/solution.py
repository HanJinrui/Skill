class Solution:

	def LargestEven(self, S):
		s = sorted(S, reverse=True)
		i = len(s) - 1
		while i >= 0 and int(s[i]) % 2 == 1:
			i -= 1
		v = s.pop(i)
		s.append(v)
		return ''.join(s)
