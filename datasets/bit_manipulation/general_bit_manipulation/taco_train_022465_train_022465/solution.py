for _ in range(int(input())):
	(a, b) = map(int, input().split())
	x = 0
	while a | x < b:
		x = x + x | 1
	print(a & ~x)
