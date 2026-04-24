(n, m) = map(int, input().split(' '))
if n == 1 or m == 1:
	print(n * m // 6 * 6 + (n * m % 6 > 3) * (n * m % 6 % 3 * 2))
elif n * m < 6:
	print(0)
elif n * m == 6:
	print(4)
elif n * m == 14:
	print(12)
else:
	print(n * m - n * m % 2)
