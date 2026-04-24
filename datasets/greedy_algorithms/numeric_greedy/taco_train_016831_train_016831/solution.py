for i in range(int(input())):
	(n, m, k) = map(int, input().split())
	s = m + k
	print(max(1, min(n, s - n + 1)), min(n, s - 1))
