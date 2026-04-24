from bisect import bisect_left as lb
(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
p = [sorted(list(set(a[i]))) for i in range(n)]
b = [list((a[i][j] for i in range(n))) for j in range(m)]
q = [sorted(list(set(b[i]))) for i in range(m)]
ans = [[0] * m for i in range(n)]
for i in range(n):
	for j in range(m):
		x = lb(p[i], a[i][j])
		y = lb(q[j], a[i][j])
		ans[i][j] = max(x, y) + max(len(p[i]) - x, len(q[j]) - y)
for i in range(n):
	print(*ans[i])
