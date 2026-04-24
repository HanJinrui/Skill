for _ in [0] * int(input()):
	(a, b, c) = map(int, input().split())
	print(max(0, min(c + 1, a - b + c + 1 >> 1)))
