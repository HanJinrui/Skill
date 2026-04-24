for _ in range(int(input())):
	(n, m) = list(map(int, input().split()))
	if n == m:
		s = '01' * (n + 1)
	elif n > m:
		s = '01' * m + '010' * (n - m)
	else:
		s = '10' * n + '101' * (m - n)
	print(len(s))
	print(s)
