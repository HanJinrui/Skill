for tc in range(int(input())):
	(n, k) = [int(a) for a in input().split()]
	a = [0] + [int(a) for a in input().split()]
	res = []
	for i1 in range(1, n):
		while a[i1] != i1 and a[a[i1]] != i1:
			i2 = a[i1]
			i3 = a[i2]
			res += [[i1, i2, i3]]
			(a[i2], a[i3], a[i1]) = (i2, i3, a[i3])
	pair = [(i1, a[i1]) for i1 in range(1, n + 1) if a[i1] > i1]
	if len(pair) % 2:
		print(-1)
	else:
		while pair:
			(i1, i2) = pair.pop()
			(i3, i4) = pair.pop()
			res += [[i1, i2, i3], [i1, i4, i3]]
		print(len(res), *['\n' + ' '.join(map(str, r)) for r in res])
