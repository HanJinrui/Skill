for _ in range(int(input())):
	n = int(input())
	x = list(map(int, input().split()))
	y = [i for i in x if i <= n]
	y = set(y)
	print(n - len(y))
