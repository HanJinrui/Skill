for _ in ' ' * int(input()):
	a = int(input())
	x = 0
	s = 0
	for i in map(int, input().split()):
		x ^= i
		s += i
	print(2)
	print(x, s + x)
