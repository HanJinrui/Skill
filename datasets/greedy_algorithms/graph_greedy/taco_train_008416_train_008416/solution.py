t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	p = {a[i]: int(s) for (i, s) in enumerate(input().split())}
	vis = [0 for _ in range(n)]
	k = 1
	max = n - 1
	ans = 0
	for u in range(n):
		if vis[u] != 0:
			continue
		cur = u
		cnt = 0
		while vis[cur] == 0:
			vis[cur] = k
			cur = p[cur + 1] - 1
			cnt += 1
			if cnt % 2 == 0:
				ans += max
				max -= 2
	ans *= 2
	print(ans)
