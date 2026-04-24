class Solution:

	def convert(self, Str, n):
		if n == 1:
			return Str
		s = [''] * n
		cycle = 2 * (n - 1)
		for i in range(len(Str)):
			j = min(i % cycle, (cycle - i) % cycle)
			s[j] += Str[i]
		return ''.join(s)
