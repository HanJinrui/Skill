a = []
res = []
n = int(input())
for i in range(n):
	a.append(list(map(int, input().split())))
for j in range(n):
	if a[j][2] >= 0:
		(q, c) = (0, 0)
		for k in range(j + 1, n):
			if a[k][2] >= 0:
				a[k][2] -= q + max(0, a[j][0] - c)
				if a[k][2] < 0:
					q += a[k][1]
					a[k][1] = 0
				c += 1
		res.append(j + 1)
print(len(res))
print(' '.join(map(str, res)))
