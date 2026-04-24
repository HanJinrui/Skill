r = []
(n, d, l) = map(int, input().split())
for i in range(1, n):
	k = 1 if d <= 0 else l
	r.append(k)
	d = k - d
if 1 <= d <= l:
	print(*r + [d])
else:
	print(-1)
