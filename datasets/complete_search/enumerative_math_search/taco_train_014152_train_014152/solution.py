import numpy as np
mod = int(1000000000.0 + 7)

def stir(p, st, en):
	if st >= en:
		return [1, en]
	m = (st + en) // 2
	ret = np.polymul(stir(p, st, m), stir(p, m + 1, en))
	return np.mod(ret, p)
for _ in range(int(input())):
	(n, p) = map(int, input().split())
	nst = 1 if n % p == p - 1 else np.sum(stir(p, 1, n % p) != 0)
	n = (n + 1) // p
	while n > 0:
		(nst, n) = (nst * (n % p + 1) % mod, n // p)
	print(nst)
