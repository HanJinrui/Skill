for _ in range(int(input())):
	p = sum([{'T': 2, 'S': 1}[i] for i in input()])
	o = int(input()) * 12
	x = o // p
	print(o * x - p * sum(range(x + 1)))
