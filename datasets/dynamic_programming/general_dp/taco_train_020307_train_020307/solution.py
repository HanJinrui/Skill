for _ in range(int(input())):
	(N, K) = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	M = max(sum(A), sum(B)) + 1
	dp = [[-1 for s in range(M)] for i in range(K + 1)]
	dp[0][0] = 0
	for i in range(N):
		for j in range(K - 1, -1, -1):
			for s in range(M):
				s1 = s + A[i]
				if dp[j][s] != -1:
					dp[j + 1][s1] = max(dp[j + 1][s1], B[i] + dp[j][s])
	minmax = 0
	for s in range(M):
		minmax = max(minmax, min(s, dp[K][s]))
	print(minmax)
