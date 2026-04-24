(n, m) = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(m)]
b = [-1] * n
for (t, l, r) in a:
	if t == 1:
		b[l:r] = [0] * (r - l)
ok = all((min(b[l:r]) == -1 for (t, l, r) in a if t == 0))
if ok:
	b[0] = n
	for i in range(1, len(b)):
		b[i] += b[i - 1]
	print('YES')
	print(*b)
else:
	print('NO')
