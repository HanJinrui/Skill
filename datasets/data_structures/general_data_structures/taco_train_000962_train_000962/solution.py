M = 300000
mod = 1000000007

def query(q, ind):
	m = p = 0
	while ind:
		m += q[ind][0]
		p += q[ind][1]
		ind -= ind & -ind
	return (m % mod, p)

def update(q, ind, val):
	while ind < M:
		q[ind][0] = (q[ind][0] + val) % mod
		q[ind][1] += 1
		ind += ind & -ind
for _ in range(int(input())):
	n = int(input())
	c = list(map(int, input().split()))
	p = list(map(int, input().split()))
	a = list(zip(c, p))
	a.sort()
	for i in range(n):
		a[i] += (i + 1,)
	a.sort(key=lambda x: x[1])
	f = [[0, 0] for _ in range(M)]
	c = d = t = 0
	for (x, y, z) in a:
		(m, p) = query(f, z)
		t = (t + y * ((2 * p - c) * x + d - 2 * m)) % mod
		c += 1
		d += x
		update(f, z, x)
	print(t)
