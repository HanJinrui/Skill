class Solution:

	def findRollOut(self, s, roll, n):
		a = [0] * n
		for i in roll:
			a[i - 1] += 1
		c = n
		for i in range(n):
			(c, a[i]) = (c - a[i], chr(97 + (ord(s[i]) + c - 97) % 26))
		return ''.join(a)
