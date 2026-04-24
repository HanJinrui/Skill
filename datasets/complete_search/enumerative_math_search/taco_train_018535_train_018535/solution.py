(n, t) = map(int, input().split())
ar = []
for _ in range(n):
	ar.append(list(map(int, input().split())))
cur = 0
while True:
	T = float('inf')
	nums = []
	for i in range(n):
		for j in range(i):
			vd = ar[i][1] - ar[j][1]
			xd = ar[i][0] - ar[j][0]
			xd = -xd
			if vd == 0:
				continue
			if xd / vd <= 1e-06:
				continue
			if cur + xd / vd >= t:
				continue
			if xd / vd < T and abs(xd / vd - T) >= 1e-06:
				T = xd / vd
				nums = [[i, j]]
			elif abs(xd / vd - T) < 1e-06:
				nums.append([i, j])
	if T != float('inf'):
		cur += T
		for i in range(n):
			ar[i][0] += ar[i][1] * T
		for el in nums:
			(a, b) = (el[0], el[1])
			(m1, m2) = (ar[a][2], ar[b][2])
			(v1, v2) = (ar[a][1], ar[b][1])
			nv1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
			nv2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
			ar[a][1] = nv1
			ar[b][1] = nv2
	else:
		break
for i in range(n):
	ar[i][0] += ar[i][1] * (t - cur)
for i in range(n):
	print(ar[i][0])
