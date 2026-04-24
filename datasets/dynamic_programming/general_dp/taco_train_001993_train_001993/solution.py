def go(n, m):
	M = 1000000007
	f = [1, 1, 2, 4]
	for i in range(4, m + 1):
		f.append(sum(f[-4:]))
	F = [0, 1]
	for i in range(2, m + 1):
		v = f[i] = pow(f[i], n, M)
		for j in range(1, i):
			v -= F[j] * f[i - j]
		F.append(v % M)
	return F[-1]
for t in range(int(input())):
	print(go(*map(int, input().split())))
