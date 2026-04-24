for _ in range(int(input())):
	(n, m) = map(int, input().split())
	a = []
	for i in range(m):
		a.append(list(map(int, input().split())))
	emp = []
	p = []
	for i in range(m - 1, -1, -1):
		if a[i][0] not in emp and a[i][1] not in emp:
			emp.append(a[i][0])
			emp.append(a[i][1])
			p.append(i)
	print(*sorted(p))
