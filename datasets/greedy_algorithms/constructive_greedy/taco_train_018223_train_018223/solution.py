for _T in range(int(input())):
	(n, m) = map(int, input().split())
	(a, b) = (input(), input())
	print('YNEOS'[a[n - m + 1:] != b[1:] or b[0] not in a[:n - m + 1]::2])
