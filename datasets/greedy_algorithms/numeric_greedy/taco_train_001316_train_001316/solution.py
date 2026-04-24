for _ in range(int(input())):
	(a, b) = map(int, input().split())
	n = 1
	for i in list(map(int, input().split())):
		if i == n:
			n += 1
	print((a - n + b) // b)
