import sys
input = sys.stdin.buffer.readline
(n, k, q) = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7
pcc = [1] * n * (k + 1)
for i in range(k):
	pcc[(i + 1) * n + 0] = pcc[i * n + 1]
	pcc[(i + 1) * n + n - 1] = pcc[i * n + n - 2]
	for p in range(1, n - 1):
		pcc[(i + 1) * n + p] = (pcc[i * n + p - 1] + pcc[i * n + p + 1]) % MOD
cc = [0] * n
for p in range(n):
	for i in range(k + 1):
		cc[p] = (cc[p] + pcc[i * n + p] * pcc[(k - i) * n + p]) % MOD
sm = 0
for p in range(n):
	sm = (sm + a[p] * cc[p]) % MOD
for _ in range(q):
	(p, x) = map(int, input().split())
	p -= 1
	sm = (sm + cc[p] * (x - a[p])) % MOD
	a[p] = x
	print(sm)
