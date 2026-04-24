class Solution:

	def kPalindrome(self, str, n, k):
		a = str
		b = str[::-1]
		c = 0
		for i in range(n):
			if a[i] != b[i]:
				if n % 2 == 0 and i == n // 2:
					c -= 1
				c += 1
		if c > k:
			return 0
		return 1
