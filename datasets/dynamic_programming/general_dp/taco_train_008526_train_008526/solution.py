def stain_combos(n, k):
	p = 1000000007
	if k < 0:
		return 0
	out = 1
	for i in range(n - k + 1, n + 1):
		out = out * i % p
	denom = 1
	for i in range(1, k + 1):
		denom = denom * i % p
	denom = pow(denom, p - 2, p)
	return out * denom % p

def solve(n, k, stains):
	print(size_decrease(stains, k))
from itertools import combinations
from functools import reduce

def size_decrease(stains, k):
	min_x = min([p.x for p in stains])
	max_x = max([p.x for p in stains])
	min_y = min([p.y for p in stains])
	max_y = max([p.y for p in stains])
	top = {p for p in stains if p.x == min_x}
	bot = {p for p in stains if p.x == max_x}
	left = {p for p in stains if p.y == min_y}
	right = {p for p in stains if p.y == max_y}
	out = 0
	for i in range(1, 5):
		for sides in combinations([top, bot, left, right], i):
			removed = reduce(lambda x, y: x.union(y), sides)
			length = len(removed)
			out += (-1) ** (i + 1) * stain_combos(len(stains) - length, k - length)
	return out % 1000000007
from collections import namedtuple
point = namedtuple('point', ['x', 'y'])
(n, k) = [int(x) for x in input().split(' ')]
stains = []
for _ in range(n):
	stains.append(point(*[int(number) for number in input().split(' ')]))
solve(n, k, stains)
