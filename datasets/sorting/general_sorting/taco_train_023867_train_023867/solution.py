from math import ceil
tt = 24 * 60 * 60 * 7
for _ in range(int(input())):
	tc = 0
	cl = []
	for __ in range(7):
		a = list(map(int, input().split()))
		dc = a[0]
		tc += dc
		for i in range(1, dc*2, 2):
			cl.append(a[i+1] - a[i])
	cl.sort()
	tc = int(ceil(tc*3/4.0))
	print(tt - sum(cl[:tc]))
