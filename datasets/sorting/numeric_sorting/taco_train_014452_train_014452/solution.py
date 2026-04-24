(n, k) = map(int, input().split())
a = list(map(int, input().split()))
c = len(a)
while c and k // c:
	t = k // c
	v = 0
	for i in range(len(a)):
		if a[i] == 0:
			continue
		v += a[i] - max(0, a[i] - t)
		a[i] = max(0, a[i] - t)
		if a[i] == 0:
			c -= 1
	k -= v
for i in range(len(a)):
	if k == 0:
		break
	if a[i] != 0:
		k -= 1
		a[i] -= 1
res = []
for j in range(len(a)):
	if a[(j + i) % len(a)] != 0:
		res.append(str((j + i) % len(a) + 1))
if k > 0:
	print(-1)
else:
	print(' '.join(res))
