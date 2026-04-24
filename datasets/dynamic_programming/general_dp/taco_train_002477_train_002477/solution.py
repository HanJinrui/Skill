for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	c = []
	i = 0
	while i < 2 * n:
		j = i
		while j + 1 < 2 * n and a[j + 1] < a[i]:
			j += 1
		c.append(j - i + 1)
		i = j + 1
	w = {0}
	for i in c:
		ws = set([i + j for j in w if i + j <= n])
		w = w.union(ws)
	if n in w:
		print('YES')
	else:
		print('NO')
