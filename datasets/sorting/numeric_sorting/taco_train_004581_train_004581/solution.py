import itertools
m = 10 ** 9 + 7

def factorize(n):

	def try_divisor(n, k, pfs):
		if n % k == 0:
			pfs[k] = 1
			n //= k
			while n % k == 0:
				pfs[k] += 1
				n //= k
		return n
	pfs = {}
	n = try_divisor(n, 2, pfs)
	n = try_divisor(n, 3, pfs)
	for i in itertools.count(start=1):
		n = try_divisor(n, 6 * i - 1, pfs)
		n = try_divisor(n, 6 * i + 1, pfs)
		if (6 * i + 1) ** 2 > n:
			break
	if n > 1:
		pfs[n] = 1
	return pfs
for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	assert len(a) == n
	p_lists = {}
	for x in a:
		for (p, e) in factorize(x).items():
			if p not in p_lists:
				p_lists[p] = []
			p_lists[p].append(p ** e)
	for v in p_lists.values():
		v.sort()
	sum = 0
	for __ in range(n):
		prod = 1
		for p in list(p_lists):
			ppow = p_lists[p].pop()
			if len(p_lists[p]) == 0:
				del p_lists[p]
			prod = prod * ppow % m
		sum = (sum + prod) % m
	print(sum)
