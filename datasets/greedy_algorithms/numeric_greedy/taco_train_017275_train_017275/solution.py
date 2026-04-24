for _ in range(int(input())):
	(n, x, y) = map(int, input().split())
	a = int(input(), 2)
	b = a ^ int(input(), 2)
	c = bin(b)[2:].count('1')
	if c % 2:
		print(-1)
	elif c == 2 and b & b << 1:
		print(min(2 * y, x))
	else:
		print(y * c // 2)
