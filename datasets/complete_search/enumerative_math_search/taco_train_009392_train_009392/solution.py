for i in range(int(input())):
	(r, c, a, b, x, y) = map(int, input().split())
	print(min(y - b if y >= b else 2 * c - (b + y), x - a if x >= a else 2 * r - (a + x)))
