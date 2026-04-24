for _ in range(int(input())):
	(n, z) = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort(reverse=True)
	l1 = []
	c = 0
	q = l[:]
	for j in range(z, 0, -1):
		temp = []
		for i in range(len(q) - j + 1):
			temp.append((i + 1) * q[i] + sum(q[i + 1:i + j]))
		l1.append(min(temp) + c)
		c += len(q) * q[-1]
		q = [x - q[-1] for x in q]
		j = -1
		del q[-1]
	print(min(l1))
