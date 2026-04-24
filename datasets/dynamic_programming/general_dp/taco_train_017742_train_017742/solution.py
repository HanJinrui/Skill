for _ in range(int(input())):
	N,M = list(map(int, input().strip().split()))
	arr = [[0 for i in range(M+1)] for j in range(N+1)]
	dp = [[0 for i in range(M)] for j in range(N)]
	for i in range(N):
		arr[i][:M] = list(map(int, input().strip().split()))
	for i in range(N-1,-1,-1):
		for j in range(M-1,-1,-1):
			if arr[i][j] < arr[i][j+1] and arr[i][j] < arr[i+1][j]:
				dp[i][j] = max(dp[i][j+1],dp[i+1][j])+1
			elif arr[i][j] < arr[i][j+1]:
				dp[i][j] = dp[i][j+1]+1
			elif arr[i][j] < arr[i+1][j]:
				dp[i][j] = dp[i+1][j]+1
			else:
				dp[i][j] = 1
	print(dp[0][0])
