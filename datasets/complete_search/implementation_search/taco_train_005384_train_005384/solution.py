for _ in range(int(input())):
	(a, b, c, x, y, z) = map(int, input().split())
	print(1) if a + b + c > x + y + z else print(2)
