import numpy as np
MOD = 998244353

def mpow(x, k):
	ret = 1
	x %= MOD
	while k:
		if k & 1:
			ret = ret * x % MOD
		x = x * x % MOD
		k >>= 1
	return ret

def minv(x):
	return mpow(x, MOD - 2)

def mm(a, b):
	n = a.shape[0]
	ret = np.zeros(n, dtype=int)
	for i in range(n):
		ret += b[i] * a[:, i] % MOD
	return ret % MOD
FACT = [1]
IFACT = [1]

def ch(a, b):
	return FACT[a] * IFACT[a - b] % MOD * IFACT[b] % MOD
for i in range(1, 3000):
	x = FACT[-1] * i % MOD
	FACT += [x]
	IFACT += [minv(x)]

def getEig(n):
	evals = 1 + np.arange(n) * 2 - n
	evecs = np.zeros((n, n), dtype=np.int64)
	evecs[0, :] = 1
	evecs[1, :] = evals
	for i in range(2, n):
		(a, b) = (evecs[i - 2], evecs[i - 1])
		(x, y) = (n - i + 1, i)
		c = (b * evals - x * a) % MOD
		c = c * minv(y) % MOD
		evecs[i, :] = c
	return (evals, evecs)

def getInit(n):
	ret = np.array([ch(n - 1, i) for i in range(n)], dtype=np.int64)
	ret *= minv(mpow(2, n - 1))
	return ret % MOD

def getWays(n, k):
	(x, y) = getEig(n)
	z = getInit(n) * mpow(x, k) % MOD
	return mm(y, z)

def getPairs(n, m, z):
	ret = []
	for i in range(n + 1):
		den = n - 2 * i
		if den == 0:
			if i * m == z:
				ret += [(i, j) for j in range(m + 1)]
		else:
			j = (z - i * m) // den
			if i * (m - j) + j * (n - i) == z:
				if j >= 0 and j <= m:
					ret += [(i, j)]
	return ret

def solve(n, m, q, z):
	nways = getWays(n + 1, q)
	mways = getWays(m + 1, q)
	ret = 0
	for (a, b) in getPairs(n, m, z):
		ret += nways[a] * mways[b] % MOD
	return ret % MOD
import sys
f = sys.stdin
t = int(f.readline())
for i in range(t):
	(n, m, q, z) = map(int, f.readline().split())
	print(solve(n, m, q, z))
