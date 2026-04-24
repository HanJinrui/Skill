from collections import Counter
MOD = 10 ** 9 + 7
(n, r, s) = map(int, input().split())
if (r ^ s) & 1:
	print(0)
	quit()
x = (r + s) // 2
y = (r - s) // 2
a = list(map(int, input().split()))
s = [Counter() for _ in range(n + 1)]
s[0][0] = 1
for (i, v) in enumerate(a):
	for j in range(i, -1, -1):
		s[j + 1] += Counter({k + v: e % MOD for (k, e) in s[j].items() if k + v <= x})
print(sum((c[x] * c[y] % MOD for c in s[1:])) % MOD)
