def dist(a, b):
	if -1 in (a, b):
		return 0
	return abs(a - b)
for _ in range(int(input())):
	(m, n) = [int(x) for x in input().split()]
	(a, b) = [int(x) for x in input().split()]
	dp = {-1: abs(b - a)}
	for _ in range(n - 1):
		(newa, newb) = [int(x) for x in input().split()]
		d = abs(newa - newb) + dist(b, newa)
		d2 = min((v + dist(k, newa) + abs(newa - newb) for (k, v) in dp.items()))
		for k in dp:
			dp[k] += d
		if b not in dp:
			dp[b] = float('inf')
		dp[b] = min(dp[b], d2)
		b = newb
	print(min(dp.values()))
