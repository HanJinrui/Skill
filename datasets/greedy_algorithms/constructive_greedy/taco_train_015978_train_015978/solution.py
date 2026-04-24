n = int(input())
l = []
for i in range(n):
	a = int(input())
	l.append(a)
for j in l:
	x = j // 3 + 1
	y = (j - x) // 2 + 1
	if x == y:
		x = x + 1
	z = j - x - y
	if z <= 0:
		z = 1
		y = j - x - 1
	print(y, x, z)
