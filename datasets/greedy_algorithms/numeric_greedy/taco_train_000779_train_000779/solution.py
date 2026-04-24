for _ in range(int(input())):
	input()
	a = sorted(map(int, input().split()))
	if len({a1 * an for (a1, an) in zip(a, a[::-1])}) == 1 and a[::2] == a[1::2]:
		print('YES')
	else:
		print('NO')
