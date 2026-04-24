n = int(input())
if n == 3:
	print(5)
else:
	x = 1
	xx = 1
	while xx < n:
		x += 2
		xx = x * x // 2 + 1
	print(x)
