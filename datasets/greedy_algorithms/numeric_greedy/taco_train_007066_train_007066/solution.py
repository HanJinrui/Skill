T = int(input())
for i in range(T):
	N = int(input())
	a = 0
	for x in [100, 50, 10, 5, 2, 1]:
		y = N // x
		N -= y * x
		a += y
	print(a)
