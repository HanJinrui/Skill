for _ in range(int(input())):
	n = int(input())
	a = input()
	x = a.count('1')
	y = n - x
	p = 2 * min(x, y)
	q = min(abs(x - y), 1)
	print(p + q)
