import random
SIZE = 900

def R():
	return map(int, input().split())

def ask(i):
	print('?', i, flush=True)
	(v, nxt) = R()
	if v < 0:
		exit()
	return (v, nxt)
(n, s, x) = R()
q = range(1, n + 1)
if n > SIZE:
	q = random.sample(q, SIZE)
(v, nxt) = max((t for t in map(ask, q) if t[0] < x), default=(-1, s))
while v < x and ~nxt:
	(v, nxt) = ask(nxt)
print('!', v if v >= x else -1)
