for _ in range(int(input())):
	n = int(input())
	a = []
	for i in range(1, n + 1, 2):
		while i <= n:
			a.append(i)
			i *= 2
	print(2)
	print(*a)
