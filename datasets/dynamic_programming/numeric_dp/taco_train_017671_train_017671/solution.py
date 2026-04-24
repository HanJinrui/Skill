class Solution:

	def ncr(self, n, r):
		p = 1000000007
		num = den = 1
		for i in range(r):
			num = num * (n - i) % p
			den = den * (i + 1) % p
		return num * pow(den, p - 2, p) % p
