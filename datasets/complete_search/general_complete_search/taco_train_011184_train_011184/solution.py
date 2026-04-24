N = 10
a = [0] * (2 << 2 * N + 1)
b = [0] * 4
n = int(input())
K = 0
t = 0
for x in map(int, input().split()):
	K |= x - 1 << t * 2
	t += 1
a[0] = 1
Q = []
Q.append(0)
ind = 0
while True:
	x = Q[ind]
	ind += 1
	if x == K:
		print(a[x] - 1)
		exit(0)
	for i in range(4):
		b[i] = 1000
	for i in range(n - 1, -1, -1):
		b[3 & x >> i * 2] = i
	for i in range(4):
		for j in range(4):
			if b[i] < b[j]:
				y = x + (j - i << b[i] * 2)
				if a[y] == 0:
					a[y] = a[x] + 1
					Q.append(y)
