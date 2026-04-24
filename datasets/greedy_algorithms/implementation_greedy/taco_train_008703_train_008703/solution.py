I = input
for _ in [0] * int(I()):
	(n, m, k) = map(int, I().split())
	a = [[*I()] for _ in [0] * n]
	f = 0
	while n:
		n -= 1
		for i in range(m):
			j = 0
			while j <= min(i, m - i - 1, n) and (t := a[n - j])[i - j] < '.' > t[i + j]:
				j += 1
			f |= a[n][i] == '*' and j <= k
			if j > k:
				while j:
					j -= 1
					t = a[n - j]
					t[i - j] = t[i + j] = '#'
	print('YNEOS'[f::2])
