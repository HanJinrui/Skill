from math import gcd
for q in range(int(input())):
	(r, b, k) = map(int, input().split())
	(r, b) = (min(r, b), max(r, b))
	print('REBEL' if r * (k - 1) + gcd(r, b) < b else 'OBEY')
