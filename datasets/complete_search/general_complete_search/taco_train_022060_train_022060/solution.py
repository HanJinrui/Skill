for _ in range(int(input())):
	(N, M) = [int(s) for s in input().split()]
	cost1 = cost2 = 0
	for i in range(N):
		for (j, c) in enumerate(input()):
			if i + j & 1 == (c != 'R'):
				cost2 += 5 if c == 'R' else 3
			else:
				cost1 += 5 if c == 'R' else 3
	print(min(cost1, cost2))
