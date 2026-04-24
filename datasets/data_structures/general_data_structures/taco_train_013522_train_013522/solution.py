for _ in range(int(input())):
	(N, M, K) = [int(s) for s in input().split()]
	if N * M <= 2:
		print(0)
	elif N == 1 or M == 1:
		print(K)
	else:
		print(K - K // 2)
