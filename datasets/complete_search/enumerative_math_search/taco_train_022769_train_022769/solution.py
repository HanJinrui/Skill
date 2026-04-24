from math import gcd
(n, k) = map(int, input().split())
(a, b) = map(int, input().split())
res = set()
for i in range(100000):
	res.add(n * k // gcd(a + b + k * i, n * k))
	res.add(n * k // gcd(a - b + k * i, n * k))
print(min(res), max(res))
