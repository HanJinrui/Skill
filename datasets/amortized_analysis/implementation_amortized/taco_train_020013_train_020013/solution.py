(n, m) = map(int, input().split())
(l, r) = (1, n)
for i in range(m):
	a = input().split()
	if a[2] == 'left':
		r = min(r, int(a[4]) - 1)
	else:
		l = max(l, int(a[4]) + 1)
print(r - l + 1 if l <= r else -1)
