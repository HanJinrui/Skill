import math
t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	s = input()
	ans = n * k
	for j in s:
		v = ord(j) - 96
		if v > 2 * k:
			ans += v - 2 * k
	n = ans
	d = k
	gcd = math.gcd(n, d)
	n //= gcd
	d //= gcd
	print(str(n) + ' ' + str(d))
