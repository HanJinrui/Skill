n = int(input())
(a, mi) = (1, 999999999999)
while a ** 3 <= n:
	if n % a == 0:
		b = 1
		while b ** 2 <= n // a:
			if n // a % b == 0:
				c = n // a // b
				mi = min(mi, (a + 1) * (b + 2) * (c + 2))
			b += 1
	a += 1
print(mi - n, 9 * n + 9 - n)
