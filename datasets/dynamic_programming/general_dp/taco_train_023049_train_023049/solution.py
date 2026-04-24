(n, l, k) = map(int, input().split())
a = list(map(int, input().split())) + [l]
b = list(map(int, input().split())) + [0]
dp = {}

def dfs(i, k, p):
	if (i, k, p) in dp:
		return dp[i, k, p]
	if i == n:
		return 0
	res = float('inf')
	if k > 0 and b[i] > p:
		res = min(res, p * (a[i + 1] - a[i]) + dfs(i + 1, k - 1, p))
	res = min(res, b[i] * (a[i + 1] - a[i]) + dfs(i + 1, k, b[i]))
	dp[i, k, p] = res
	return res
print(a[1] * b[0] + dfs(1, k, b[0]))
