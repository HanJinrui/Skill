for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = list((i for i in map(int, input().split()) if i > k))
	print(len(a))
