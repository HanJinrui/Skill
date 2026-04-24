import math, sys
input = sys.stdin.readline
S = lambda : input().rstrip()
I = lambda : int(S())
M = lambda : map(int, S().split())
L = lambda : list(M())
mod1 = 1000000007
mod2 = 998244353
fact = [1] * 10000
for i in range(1, 10000):
	fact[i] = fact[i - 1] * i % mod1
for _ in range(I()):
	n = I()
	a = L()
	s1 = set()
	s2 = set()
	s3 = set()
	if 0 not in a:
		print(0)
		continue
	for i in range(n):
		if a[i] == 0:
			s1.add(i + 1)
		else:
			s2.add(a[i])
	for i in range(1, n + 1):
		if i not in s2:
			s3.add(i)
	k = len(s1 & s3)
	t = len(s1)
	ans = fact[t]
	for i in range(1, k + 1):
		p = fact[k] * pow(fact[k - i], mod1 - 2, mod1) * pow(fact[i], mod1 - 2, mod1) * fact[t - i] % mod1
		if i % 2 == 1:
			ans = (ans - p) % mod1
		else:
			ans = (ans + p) % mod1
	print(ans)
