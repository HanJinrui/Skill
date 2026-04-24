import sys
input = sys.stdin.readline
mod = 10 ** 9 + 7
N = 10 ** 5
(F, iF) = ([0] * (N + 1), [0] * (N + 1))
F[0] = 1
for i in range(1, N + 1):
	F[i] = F[i - 1] * i % mod
iF[-1] = pow(F[-1], mod - 2, mod)
for i in range(N - 1, -1, -1):
	iF[i] = iF[i + 1] * (i + 1) % mod

def cal(n, k):
	if k < 0 or k > n:
		return 0
	return F[n] * iF[k] * iF[n - k] % mod
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	ans = 1
	x = 1
	while n - (k - 1) * (x - 1) >= x:
		ans = (ans + cal(n - (k - 1) * (x - 1), x) * pow(cal(n, x), mod - 2, mod)) % mod
		x += 1
	print(ans)
