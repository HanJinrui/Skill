import sys
input = sys.stdin.readline

def getp(p, x):
	if p[x] == x:
		return x
	else:
		p[x] = getp(p, p[x])
		return p[x]

def solve():
	(n, m, k) = map(int, input().split())
	c = list(map(int, input().split()))
	d = dict()
	for i in range(m):
		(u, v) = map(int, input().split())
		z = c[u - 1] ^ c[v - 1]
		if z in d:
			d[z].append((u - 1, v - 1))
		else:
			d[z] = [(u - 1, v - 1)]
	MOD = int(1000000000.0 + 7)
	res = pow(2, n, MOD) * ((2 ** k - len(d)) % MOD) % MOD
	p = list(range(n))
	for z in d:
		e = d[z]
		c = n
		for (u, v) in e:
			u = getp(p, u)
			v = getp(p, v)
			if u != v:
				p[u] = v
				c -= 1
		for (u, v) in e:
			p[u] = u
			p[v] = v
		res = (res + pow(2, c, MOD)) % MOD
	print(res)
solve()
