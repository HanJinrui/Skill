from itertools import chain, cycle, islice, repeat
from operator import itemgetter
d = 26
a = ord('a')
t = input()
n = len(t)
p = [0] * n
for b in (d ** 2, d, 1):
	if n >= b:
		q = (repeat(chr(a + i), b) for i in range(d))
		q = chain.from_iterable(q)
		q = cycle(q)
		q = islice(q, n)
		q = ''.join(q)
		print('?', q, flush=True)
		s = input()
		for (i, c) in enumerate(s):
			p[i] += b * (ord(c) - a)
p = zip(range(n), p)
p = sorted(p, key=itemgetter(1))
p = next(zip(*p))
ans = list(t)
ans = ''.join((ans[p[i]] for i in range(n)))
print('!', ans, flush=True)
