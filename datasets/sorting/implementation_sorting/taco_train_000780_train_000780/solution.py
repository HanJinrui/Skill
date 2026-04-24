x1 = int(input())
for i in range(x1):
	z = int(input())
	l = input().split(' ')
	x = -1
	d = {}
	for j in l:
		if j not in d:
			d[j] = 1
		elif d[j] >= 2:
			x = j
		elif d[j] < 2:
			d[j] += 1
	print(x)
