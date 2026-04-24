for _ in range(int(input())):
	n, k = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	dp = [0]*n
	for i in range(k + 1):
		dp[i] = max(arr[i], dp[i - 1])
	for i in range(k + 1, n):
		dp[i] = max(arr[i] + dp[i - k - 1], dp[i - 1])
	print(dp[-1])
