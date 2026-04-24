for s in [0] * int(input()):
	n = int(input())
	print(n % 2050 and -1 or sum(map(int, str(n // 2050))))
