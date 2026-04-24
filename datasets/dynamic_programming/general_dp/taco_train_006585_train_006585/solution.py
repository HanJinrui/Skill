def solve(ar):
	dp = [0] + [9223372036854775807] + [0] * (len(ar) - 1)
	dp[2] = ar[1] - ar[0]
	for i in range(3, len(ar) + 1):
		dp[i] = min(dp[i - 2] + ar[i - 1] - ar[i - 2], dp[i - 3] + ar[i - 1] - ar[i - 3])
	return dp[len(ar)]

def cr(arr, ar):
	for i in range(len(arr)):
		if arr[i]:
			ar.append(i)
	return ar
for _ in range(int(input())):
	(n, ls) = (int(input()), list(map(int, input().split())))
	ar = cr(ls, [])
	print(-len(ar)) if len(ar) == 0 or len(ar) == 1 else print(min((solve(ar), solve(cr(ls[-(n - ar[-1]):] + ls[:-(n - ar[-1])], [])), solve(cr(ls[-(n - ar[-2]):] + ls[:-(n - ar[-2])], [])))))
