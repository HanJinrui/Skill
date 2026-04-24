for i in range(int(input())):
	x = int(input())
	y = ''
	for _ in range(x):
		y += input()
	y = [y.count(l) for l in ['c', 'o', 'd', 'e', 'h', 'f']]
	y[0] //= 2
	y[3] //= 2
	print(min(y))
