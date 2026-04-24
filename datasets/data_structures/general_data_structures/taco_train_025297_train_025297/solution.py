for _ in range(int(input())):
	a = input()
	l = list(map(int, input().split()))
	(r, m) = (0, l[0])
	for i in l:
		if i < m:
			m = i
		r += m
	print(r)
