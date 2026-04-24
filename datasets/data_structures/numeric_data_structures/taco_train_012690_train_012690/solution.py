for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	(o, e) = (0, 0)
	for i in a:
		if i % 2:
			o += 1
		else:
			e += 1
	ne = n // 2
	no = n - ne
	print(min(no, e) + min(ne, o))
