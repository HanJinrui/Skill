class Solution:

	def nthprimedigitsnumber(self, n):
		t = ''
		s = {1: '2', 2: '3', 3: '5', 0: '7'}
		while n != 0:
			t += s[n % 4]
			if n % 4 == 0:
				n = n - 1
			n = n // 4
		return t[::-1]
