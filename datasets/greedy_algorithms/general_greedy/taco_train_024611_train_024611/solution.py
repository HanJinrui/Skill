n = int(input())
a = list(sorted(map(int, input().split())))
(p, q) = map(int, input().split())

def f(m):
	if m < p or m > q:
		return 0
	r = 1 << 32
	for i in a:
		r = min(r, abs(i - m))
	return r
ans = max((f(p), -p), (f(q), -q))
for i in range(1, n):
	m = (a[i] + a[i - 1]) // 2
	ans = max(ans, (f(m), -m))
print(-ans[1])
