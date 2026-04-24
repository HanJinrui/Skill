(n, m) = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
	(t, l, r) = map(int, input().split())
	l -= 1
	if t == 1:
		for i in range(l, r, 2):
			(a[i], a[i + 1]) = (a[i + 1], a[i])
	else:
		print(sum(a[l:r]))
