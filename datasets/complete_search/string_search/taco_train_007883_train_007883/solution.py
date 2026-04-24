n = int(input())
a = (*map(int, input().split()),)
d = {}
for i in range(n):
	for j in range(i):
		s = a[i] + a[j]
		if s not in d:
			d[s] = (i, j)
		else:
			x = d[s]
			if i not in x and j not in x:
				print('YES')
				print(x[0] + 1, x[1] + 1, i + 1, j + 1)
				exit()
print('NO')
