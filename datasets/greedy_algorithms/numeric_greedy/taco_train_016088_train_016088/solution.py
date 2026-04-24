for _ in range(int(input())):
	(s, n) = map(int, input().split())
	while s != 0:
		if n == 1:
			print(s)
			break
		cu = 1
		while cu * 10 <= s - n + 1:
			cu *= 10
		s -= cu
		print(cu, end=' ')
		n -= 1
