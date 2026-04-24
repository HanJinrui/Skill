for _ in range(int(input())):
	(n, m, k) = map(int, input().split())
	a = list(map(int, input().split()))
	freeCells = n * m - (n + m - 1)
	buffers = n * m - freeCells - 4
	for i in range(k):
		if i - k + a[i] > freeCells + buffers:
			print('TIDAK')
			break
	else:
		print('YA')
