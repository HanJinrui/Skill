def ch(a, b, c, d, e, f):
	(d1, d2, d3) = (abs(a - d), abs(b - e), abs(c - f))
	if a + b + c == 0 or d + e + f == 0:
		print(2) if d1 % 2 == d2 % 2 and d2 % 2 == d3 % 2 else print(1)
	else:
		print(0) if (d1 % 2 + d2 % 2 + d3 % 2) % 3 == 0 else print(1)
for z in range(int(input())):
	(a, b, c, d, e, f) = map(int, input().split())
	print(0) if a == d and b == e and (c == f) else ch(a, b, c, d, e, f)
