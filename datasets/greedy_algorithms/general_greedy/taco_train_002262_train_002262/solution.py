(n, m) = map(int, input().split())
ll = [[] for i in range(n - 1)]
for i in range(m):
	a = list(map(int, input().split()))
	for j in range(n - 1):
		ll[j].append([a[-1] - a[j], i])
mi = 10000000
for l in ll:
	l.sort()
	s = sum([l[j][0] for j in range(m)])
	temp = []
	j = 1
	while s > 0:
		temp.append(l[-j][1])
		s -= l[-j][0]
		j += 1
	if len(temp) < mi:
		mi = len(temp)
		ans = temp[:]
print(mi)
print(*[i + 1 for i in ans])
