def transpos(a, n, m):
	b = []
	for i in range(m):
		b.append([a[j][i] for j in range(n)])
	return b

def printarr(a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			print(a[i][j], end=' ')
		print('')
(n, m) = [int(i) for i in input().split()]
a = []
for i in range(n):
	a.append([i * m + j for j in range(1, m + 1)])
transp_flag = False
if n > m:
	tmp = m
	m = n
	n = tmp
	a = transpos(a, m, n)
	transp_flag = True
if m < 3 and m != 1:
	print('NO')
elif m == 1:
	print('YES')
	print(1)
else:
	if m == 3:
		if n < 3:
			print('NO')
		else:
			print('YES')
			printarr([[5, 9, 3], [7, 2, 4], [1, 6, 8]])
	elif m == 4:
		for i in range(n):
			tmp = a[i][:]
			if i % 2 == 0:
				a[i] = [tmp[1], tmp[3], tmp[0], tmp[2]]
			else:
				a[i] = [tmp[2], tmp[0], tmp[3], tmp[1]]
	else:
		for i in range(n):
			if i % 2 == 0:
				tmp1 = [a[i][j] for j in range(m) if j % 2 == 0]
				tmp2 = [a[i][j] for j in range(m) if j % 2 == 1]
			if i % 2 == 1:
				tmp1 = [a[i][j] for j in range(m) if j % 2 == 1]
				tmp2 = [a[i][j] for j in range(m) if j % 2 == 0]
			a[i] = tmp1 + tmp2
	if m > 3:
		if transp_flag:
			a = transpos(a, n, m)
		print('YES')
		printarr(a)
