t = int(input())
for test in range(t):
	(l, r) = map(int, input().split())
	a = list(map(int, input().split()))
	for j in range(17):
		if (r - l + 1) % pow(2, j + 1) != 0:
			break
	b = a
	visit = set()
	if j > 0:
		for i in range(r - l + 1):
			visit.add(a[i] >> j)
		b = list(visit)
	xor = 0
	for x in range(l, r + 1, pow(2, j)):
		xor ^= x >> j
	for x in b:
		xor ^= x
	print(xor * pow(2, j))
