for _ in range(int(input())):
	l = int(input())
	a = list(map(int, input().split()))
	for i in range(1, len(a), 2):
		x = a.pop(-1)
		a.insert(i, x)
	print(*a)
