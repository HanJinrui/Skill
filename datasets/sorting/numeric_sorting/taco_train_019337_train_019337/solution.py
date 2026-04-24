for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = sorted(list(map(int, input().split())))
	print(a[(n + k) // 2])
