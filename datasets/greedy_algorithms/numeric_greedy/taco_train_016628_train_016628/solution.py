n = int(input())
l = [int(c == 'B') for c in input()]
res = []
for e in [1, 0]:
	for i in range(n - 1):
		if l[i] == e:
			l[i] ^= 1
			l[i + 1] ^= 1
			res.append(i + 1)
	if sum(l) == (e ^ 1) * n:
		print(len(res))
		print(*res, sep=' ')
		exit(0)
print(-1)
