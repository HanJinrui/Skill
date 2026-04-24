for _ in range(int(input())):
	(a, b, c) = map(int, input().split())
	print(1 if b > c else (a + b - 1) // b)
