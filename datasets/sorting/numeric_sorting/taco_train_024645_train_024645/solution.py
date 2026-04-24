def c(a, b, k):
	v = (10 ** k - 1) // a + 1
	v -= (10 ** (k - 1) * (b + 1) - 1) // a - (10 ** (k - 1) * b - 1) // a
	return v
(MOD, v) = (1000000007, 1)
(n, k) = map(int, input().split())
for (a, b) in zip(map(int, input().split()), map(int, input().split())):
	v = v * c(a, b, k) % MOD
print(v)
