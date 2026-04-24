class Solution:

	def BoomNumber(self, K):
		t = ''
		s = {0: '2', 1: '3'}
		n = K + 1
		while n != 1:
			t += s[n % 2]
			n //= 2
		return t[::-1]
