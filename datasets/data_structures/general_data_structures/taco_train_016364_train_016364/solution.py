def QueryComputation(n, arr, k, q, queries):
	ma = 200001
	cnt = [0] * ma
	for a in arr:
		cnt[a[0] - 1] -= 1
		cnt[a[1]] += 1
	for i in range(ma - 2, -1, -1):
		cnt[i] += cnt[i + 1]
	ans = []
	for qu in queries:
		ans.append(cnt[qu] >= k)
	return ans
