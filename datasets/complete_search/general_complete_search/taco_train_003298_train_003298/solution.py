maxn = 5001
lst = [0 for _ in range(maxn)]
dp = [0 for _ in range(maxn)]
(n, m) = map(int, input().split())
for i in range(1, n + 1):
	lst[i] = i + 1
for i in range(1, m + 1):
	(l, r) = input().split(' ')
	(l, r) = (int(l), int(r))
	for j in range(l, r + 1):
		lst[j] = min(lst[j], l)
for k in range(1, m - 1):
	for i in range(n, 0, -1):
		lst_i = lst[i]
		dp[i] = max(dp[lst_i - 1] + i - lst_i + 1, dp[i])
	for i in range(1, n + 1):
		dp[i] = max(dp[i], dp[i - 1])
print(dp[n])
