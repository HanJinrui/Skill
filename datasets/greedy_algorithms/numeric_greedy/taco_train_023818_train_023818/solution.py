n = int(input())
a = []
b = [0] * (n + 1)
c = [10000] * (n + 1)
for i in range(0, n - 1):
	(p1, p2) = list(map(int, input().split()))
	a.append((p1, p2))
	b[p1] = max(b[p1], p2)
ans = []
for i in range(1, n + 1):
	if b[i] == 0:
		continue
	k = 0
	for j in range(i, n + 1):
		if b[j] == 0:
			k = j
			break
	if k == 0:
		break
	b[j] = b[i]
	b[i] = 0
	for j in range(0, n - 1):
		if a[j][0] == i:
			a[j] = (k, a[j][1])
	ans.append((1, i, k))
for i in a:
	c[i[1]] = min(c[i[1]], i[0])
for i in range(1, n + 1):
	k = i
	for j in range(i + 1, n + 1):
		if c[j] < c[i]:
			i = j
	if i == k:
		continue
	ans.append((2, i, k))
	c[0] = c[i]
	c[i] = c[k]
	c[k] = c[0]
print(len(ans))
for i in ans:
	print(i[0], i[1], i[2])
