n = int(input())
P = list(map(int, input().split()))
d = [i + 1 for i in range(n)]
qer = int(input())
for q in range(qer):
	ans = 0
	(x, k) = map(int, input().split())
	i = x - 1
	while i < n and k != 0:
		sub = min(P[i], k)
		ans += sub * (i - (x - 1))
		P[i] -= sub
		k -= sub
		if i != x - 1:
			d[x - 1] = i
		i = d[i]
	print(ans)
