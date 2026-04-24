n = int(input())
a = (*map(int, input().split()),)
c = 9000000000.0
m = 2 * n
for j in [0, 1]:
	b = list(a)
	d = 0
	while b[-1] < m:
		b = [b[n:] + b[:n], [b[i ^ 1] for i in range(m)]][j]
		j ^= 1
		d += 1
	if b < list(range(1, m + 2)):
		c = min(d, c)
print([-1, c][c < 9000000000.0])
