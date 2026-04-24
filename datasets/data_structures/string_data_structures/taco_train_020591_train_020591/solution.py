class Solution:

	def divisible_by_four(self, s):
		if s == '4' or s == '0' or s == '8':
			return 1
		for i in range(len(s)):
			for j in range(i + 1, len(s)):
				if int(s[i] + s[j]) % 4 == 0 or int(s[j] + s[i]) % 4 == 0:
					return 1
		return 0
