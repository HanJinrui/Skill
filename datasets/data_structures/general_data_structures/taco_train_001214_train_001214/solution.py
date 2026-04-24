t = int(input())
for _ in range(t):
	n = int(input())
	r = set()
	c = set()
	for i in range(n):
		l1 = list(map(int, input().split()))
		for j in range(len(l1)):
			if l1[j] == 0:
				r.add(i)
				c.add(j)
	if len(r) == n and len(c) == n:
		print('YES')
	else:
		print('NO')
