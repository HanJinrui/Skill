(n, k) = map(int, input().split())
a = list(map(int, input().split()))

def f(i, p):
	if p > k:
		return 0
	if i == -1:
		return 1
	if p not in dp[i]:
		dp[i][p] = f(i - 1, p) + f(i - 1, p * a[i])
	return dp[i][p]
dp = [{} for i in range(n)]
ans = f(n - 1, 1) - 1
print(ans)
