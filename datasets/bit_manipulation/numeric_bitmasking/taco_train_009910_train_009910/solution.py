for _ in range(int(input())):
	n = 1 << list(map(int, input().split()))[0]
	print((n - 1) * (n - 2))
