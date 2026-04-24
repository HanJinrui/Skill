from math import gcd
(n, m) = map(int, input().split())
SUM = 0
sum = m
L = 2
k = m ** 2
for i in range(2, n + 1):
	if gcd(i, L) == 1 and L <= 10 ** 12:
		L *= i
	sum *= m // L
	sum = sum % 998244353
	SUM += k - sum
	k *= m
	k = k % 998244353
print(SUM % 998244353)
