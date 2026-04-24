import math
t = int(input())
for x in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	s = 0
	for i in a:
		s += i
	bits = [0] * 20
	msb = [0] * 20
	t = [[0 for z in range(20)] for j in range(20)]
	for i in range(n):
		if a[i] == 0:
			continue
		k = int(math.log(a[i], 2))
		msb[k] += 1
		for j in range(20):
			bv = a[i] >> j & 1
			bits[j] += bv
			t[k][j] += bv
	res = 0
	for i in range(n):
		if b[i] == 0:
			res += s
			continue
		k = int(math.log(b[i], 2))
		for j in range(20):
			bv = b[i] >> j & 1
			if bv == 0:
				res += (bits[j] - t[k][j]) * (1 << j)
			else:
				res += t[k][j] * (1 << j)
				res += (n - bits[j] - (msb[k] - t[k][j])) * (1 << j)
	print(res)
