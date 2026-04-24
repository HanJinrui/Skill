for _ in [0] * int(input()):
	n = int(input())
	a = set()
	for x in map(int, input().split()):
		while x % 2 == 0:
			a.add(x)
			x /= 2
	print(len(a))
