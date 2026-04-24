for _ in range(int(input())):
	(S, C, K) = map(int, input().split())
	if K == 1:
		print((1 << max(S, C + 1)) + 1 if S else (1 << C) - 1 << 1)
	elif K <= S and K - 1 + C >= S:
		print((1 << S - K + 2) + 1)
	elif K <= S:
		print((1 << S - K + 1) + 1)
	else:
		print(0)
