for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	if n == 2:
		print(min(a))
	elif n >= 3:
		l = []
		(d1, d2, d3) = (a[2] - a[0], a[2] - a[1], a[1] - a[0])
		for i in [d1, d3]:
			(x, y, count) = (a[0], 1, 0)
			while y < n:
				if a[y] - x != i:
					count += 1
					res = a[y]
				else:
					x = a[y]
				y += 1
				if count >= 2:
					break
			if count == 1:
				l.append(res)
			elif count == 0:
				l.append(min(a[0], a[-1]))
		(x, y, count) = (a[1], 2, 0)
		while y < n:
			if a[y] - x != d2:
				count += 1
				break
			x = a[y]
			y += 1
		if count == 0:
			l.append(a[0])
		if len(l) == 0:
			print(-1)
		else:
			print(min(l))
