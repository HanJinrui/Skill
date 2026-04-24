from collections import Counter
l1 = input().split(' ')
(n, m) = (int(l1[0]), int(l1[1]))
tiles = Counter(map(int, input().split(' ')))
nums = sorted(tiles)
dp = {(0, 0): 0}
for num in nums:
	(v0, v1) = (tiles[num], tiles[num + 1])
	new_dp = Counter()
	for ((d0, d1), c) in dp.items():
		(t0, t1) = (v0 - d0, v1 - d1)
		for d in range(min(t0, t1, 2) + 1):
			k = (d1 + d, d)
			new_dp[k] = max(new_dp[k], c + d + (t0 - d) // 3)
	dp = new_dp
print(max(dp.values()))
