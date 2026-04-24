for t in range(int(input())):
	(n, x) = [int(i) for i in input().split()]
	ai = [int(i) for i in input().split()]
	count = 0
	for i in ai:
		if i % 2 == 0:
			count += 1
	print(int((count + 1) / 2) if x % 2 != 0 else -1 if count == n else count)
