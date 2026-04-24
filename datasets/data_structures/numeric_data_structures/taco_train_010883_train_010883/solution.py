from math import gcd

def lcm(x, y):
	if max(x, y) > 10 ** 9:
		return 10 ** 9 + 1
	ans = x * y // gcd(x, y)
	return ans if ans <= 10 ** 9 else 10 ** 9 + 1
mod = 998244353
for _ in range(int(input())):
	n = int(input())
	a = [tuple(map(int, input().split())) for _ in range(n)]
	a.sort(key=lambda xx: xx[0])
	pref = [1]
	suff = [0]
	for i in range(n):
		pref.append(lcm(pref[-1], a[i][0]))
	for i in range(n - 1, -1, -1):
		suff.append(gcd(suff[-1], a[i][0]))
	suff.reverse()
	(ans, prev) = (0, 0)
	for i in range(1, n + 1):
		if not suff[i - 1] % pref[i]:
			ans = (ans + pow(2, a[i - 1][1], mod) - prev - (i == 1) - (i == n)) % mod
			prev = 1
		else:
			prev = 0
	print(ans)
