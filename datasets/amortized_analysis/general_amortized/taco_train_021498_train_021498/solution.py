for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	c = 0
	for i in range(n - 1, -1, -1):
		if a[i] != b[i + c]:
			c += 1
	print(c)
