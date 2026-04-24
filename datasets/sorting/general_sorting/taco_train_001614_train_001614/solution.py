for i in range(int(input())):
	n = int(input())
	l = sorted(list(map(int, input().split())))
	for i in range(1, n - 1, 2):
		(l[i], l[i + 1]) = (l[i + 1], l[i])
	print(*l)
