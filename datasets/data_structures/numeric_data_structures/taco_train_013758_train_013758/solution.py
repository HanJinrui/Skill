from math import gcd
(n, d1, d2) = (int(input()), 0, 0)
for e in map(int, input().split()):
	(d2, d1) = (gcd(d2, d1 * e), gcd(d1, e))
print(d2 // d1)
