for i in range(int(input())):
	n = int(input())
	b = list(map(int, input().split()))
	a = list(set(b))
	c = []
	a.sort()
	for i in range(len(a)):
		c.append(a[i // 2])
		c.append(a[(len(a) - 1 + i) // 2])
	c.sort()
	b.sort()
	if c == b:
		print(*a)
	else:
		print(-1)
