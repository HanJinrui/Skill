for _ in range(int(input())):
	(n, x) = map(int, input().split())
	print(min(len(set(map(int, input().split()))), n - x))
