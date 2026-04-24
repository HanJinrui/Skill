mod = 10 ** 9 + 7
cache = {0: (0, 1), 1: (1, 1)}

def fib_pair(n):
	if n in cache:
		return cache[n]
	hn = n // 2
	(f, fp) = fib_pair(hn)
	if n & 1:
		res = ((fp * fp + f * f) % mod, (2 * f + fp) * fp % mod)
	else:
		fm = fp - f
		if fm < 0:
			fm += mod
		res = ((2 * fm + f) * f % mod, (fp * fp + f * f) % mod)
	if n < 1000000:
		cache[n] = res
	return res
(n, m) = map(int, input().strip().split())
parents = (n + 1) * [0]
children = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
	j = int(input())
	parents[i] = j
	children[j].append(i)
depths = (n + 1) * [0]
stack = [(1, 1)]
while stack:
	(i, d) = stack.pop()
	depths[i] = d
	for j in children[i]:
		stack.append((j, d + 1))
nrs = (n + 1) * [0]
for _ in range(m):
	(q, si, sj) = input().strip().split()
	if q == 'U':
		(x, k) = (int(si), int(sj))
		fibs = list(fib_pair(k))
		stack = [(x, 0)]
		while stack:
			(y, l) = stack.pop()
			if l >= len(fibs):
				fibs.append((fibs[-1] + fibs[-2]) % mod)
			nrs[y] += fibs[l]
			for z in children[y]:
				stack.append((z, l + 1))
	else:
		(i, j) = (int(si), int(sj))
		if depths[i] < depths[j]:
			(i, j) = (j, i)
		fsum = 0
		while depths[j] < depths[i]:
			fsum += nrs[i]
			i = parents[i]
		while i != j:
			fsum += nrs[i] + nrs[j]
			j = parents[j]
			i = parents[i]
		fsum += nrs[i]
		print(fsum % mod)
