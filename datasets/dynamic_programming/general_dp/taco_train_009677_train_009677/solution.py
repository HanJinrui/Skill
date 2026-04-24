cs = int(input())

def binom(n, r):
	if r < 0 or n < r:
		return 0
	elif n == r or r == 0:
		return 1
	else:
		return n * binom(n - 1, r - 1) // r
for c in range(cs):
	np = int(input())
	sc = [int(i) for i in input().strip().split() if int(i) != -1]
	if sum(sc) > np * (np - 1) // 2 or sc.count(0) > 1:
		print(0)
		continue
	if len(sc) == np:
		print(1)
		continue
	(n, r) = (np - len(sc), np * (np - 1) // 2 - sum(sc))
	rt = binom(r - 1, r - n)
	if 0 not in sc:
		rt += n * binom(r - 1, r - n + 1)
	print(rt)
