import os
from io import BytesIO
input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
import string

def main():
	d = 0

	class Matrix:

		def __init__(self, ar):
			self.ar = ar

		def __mul__(self, other):
			n = d
			m = d
			p = d
			ans = [[0 for i in range(p)] for i in range(m)]
			for i in range(m):
				for j in range(p):
					for k in range(n):
						ans[i][j] += self[i][k] * other[k][j]
					ans[i][j] %= mod
			return Matrix(ans)

		def __mod__(self, other):
			m = len(self[0])
			for i in range(len(self.ar)):
				for j in range(m):
					self[i][j] %= other
			return self

		def __getitem__(self, key):
			return self.ar[key]
	mod = 10 ** 9 + 7

	def power(number, n):
		res = number
		while n:
			if n & 1:
				res *= number
				n -= 1
			number *= number
			n >>= 1
		return res
	(n, m, k) = map(int, input().split())
	d = m
	m2 = Matrix([[1 for i in range(m)] for i in range(m)])
	alth = string.ascii_letters
	for i in range(k):
		s = str(input())
		temp = alth.find(s[2])
		temp2 = alth.find(s[3])
		m2[temp2][temp] = 0
	if n == 1:
		print(m)
	elif n == 2:
		print(m ** 2 - k)
	else:
		ar = power(m2, n - 2).ar
		ans = 0
		for i in range(m):
			for j in range(m):
				ans += ar[i][j]
			ans %= mod
		print(ans)
main()
