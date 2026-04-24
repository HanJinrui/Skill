def f(a):
	if p[a] < 0:
		return a
	p[a] = f(p[a])
	return p[a]

def u(a, b):
	a = f(a)
	b = f(b)
	if a == b:
		return
	if p[a] < p[b]:
		p[a] += p[b]
		p[b] = a
	else:
		p[b] += p[a]
		p[a] = b
for _ in range(int(input())):
	(n, r) = [int(x) for x in input().split()]
	p = [-1] * (n + 1)
	for i in range(r):
		(a, b) = [int(x) for x in input().split()]
		u(a, b)
	ans = 1
	count = 0
	for i in range(1, n + 1):
		if p[i] < 0:
			count += 1
			ans = ans * (-1 * p[i]) % (10 ** 9 + 7) % (10 ** 9 + 7)
	print(count, ans)
