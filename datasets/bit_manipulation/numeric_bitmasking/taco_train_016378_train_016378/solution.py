for _ in range(int(input())):
	N = int(input())
	if N == 2:
		print(-1)
	elif N % 2:
		print(*range(1, N + 1))
	else:
		print(2, 3, 1, 4, *range(5, N + 1))
