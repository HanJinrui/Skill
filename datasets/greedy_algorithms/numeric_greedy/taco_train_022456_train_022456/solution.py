for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ok = True
	for d in (0, 1):
		for i in range(d + 2, n, 2):
			ok &= a[i] & 1 == a[i - 2] & 1
	print('YES' if ok else 'NO')
