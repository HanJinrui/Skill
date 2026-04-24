r = lambda : map(int, input().split())
(n, k) = r()
a = dict(zip(r(), range(1, n + 1)))
if len(a) < k:
	print('NO')
else:
	print('YES\n', *[*a.values()][:k])
