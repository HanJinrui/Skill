for t in range(int(input())):
	n = int(input())
	l = [0] * 11
	for i in range(n):
		(x, y) = map(int, input().split())
		if l[x - 1] < y:
			l[x - 1] = y
	print(sum(l[0:8]))
