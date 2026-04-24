from collections import Counter

def bt(x, n):
	v = max(Counter(x).values())
	if v == len(x) and n == 1:
		return v - 1
	else:
		return min(v + n, len(x))
n = int(input())
d = [bt(input(), n) for _ in range(3)]
dm = max(d)
if Counter(d)[dm] > 1:
	print('Draw')
else:
	print(['Kuro', 'Shiro', 'Katie'][d.index(dm)])
