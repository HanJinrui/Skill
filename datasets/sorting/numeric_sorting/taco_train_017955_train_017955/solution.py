for _ in [0] * int(input()):
	(a, b) = map(int, input().split())
	print('NYOE S'[(a + b) % 3 < 1 and a <= 2 * b <= 4 * a::2])
