T = int(input())
for _ in range(T):
	N = int(input())
	for i in range(N):
		for j in range(N):
			if i % 2:
				print(i * N + j + 1, end=' ')
			else:
				print(i * N + N - j, end=' ')
		print()
