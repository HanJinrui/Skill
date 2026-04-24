import math
for _ in range(int(input())):
	(a, b) = map(int, input().split())
	l = list(map(int, input().split()))
	p = 0
	for i in l:
		if i >= 80 or i <= 9:
			p = p + 1
	z = math.ceil(p / b)
	c = a - p
	y = math.ceil(c / b)
	print(z + y)
