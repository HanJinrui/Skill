n = int(input())
a = list(map(int, input().split()))

def f(x):
	(mx, cur) = (0, 0)
	for i in range(n):
		cur = max(cur, 0) + a[i] - x
		mx = max(mx, cur)
	cur = 0
	for i in range(n):
		cur = max(cur, 0) + x - a[i]
		mx = max(mx, cur)
	return mx
(L, R) = (min(a), max(a) + 1)
for t in range(100):
	d = (R - L) / 3
	(x1, x2) = (L + d, R - d)
	if f(x1) > f(x2):
		L = x1
	else:
		R = x2
print('{:.10f}'.format(f(L)))
