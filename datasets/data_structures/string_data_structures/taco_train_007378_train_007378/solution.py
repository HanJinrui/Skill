class Solution:

	def isPrimeString(self, s):
		su = 0
		for i in s:
			su += ord(i)
		for i in range(2, int(su ** (1 / 2)) + 1):
			if su % i == 0:
				return 0
		return 1
