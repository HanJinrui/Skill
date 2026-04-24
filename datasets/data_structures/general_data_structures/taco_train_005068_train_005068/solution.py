for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	l1 = []
	l1 += l[n // 2:]
	l1 += l[:n // 2]
	c = 0
	for i in range(len(l)):
		if l[i] != l1[i]:
			c += 1
	print(c)
	for i in l1:
		print(i, end=' ')
	print()
