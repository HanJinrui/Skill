MOD = 10 ** 9 + 7
N = int(input())
(n, D, d, l) = (1, 0, 0, 0)
for a in map(int, input().split()):
	(n, D, d, l) = (4 * n + 2, 4 * D + (3 * n + 2) * l + (8 * n + 3) * a, 16 * a * n * n + n * 12 * (D + a) + 8 * D + a + 4 * d, 2 * l + 3 * a)
	n %= MOD
	D %= MOD
	d %= MOD
	l %= MOD
print(d % MOD)
