for i in range(int(input())):
	(n, x) = map(int, input().split())
	print(sorted(list(map(int, input().split())))[-x] - 1)
