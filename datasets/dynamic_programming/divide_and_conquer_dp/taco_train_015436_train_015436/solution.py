from math import trunc
MOD = 998244353
MODF = float(MOD)
SHRT = float(1 << 16)
fmod = lambda x: x - MODF * trunc(x / MODF)
mod_prod = lambda a, b: fmod(trunc(a / SHRT) * fmod(b * SHRT) + (a - SHRT * trunc(a / SHRT)) * b)

def fpow(a, b):
	r = 1.0
	while b:
		if b & 1:
			r = mod_prod(r, a)
		a = mod_prod(a, a)
		b >>= 1
	return r
(n, k) = map(int, input().split())
f = [0] * (5 * n + 5)
for d in map(int, input().split()):
	f[d] = 1

def ntt_transform(a, G, inv=False):
	(n, k) = (1, 0)
	while n < len(a):
		k += 1
		n *= 2
	a += [0] * (n - len(a))
	n2 = n // 2
	w = [1] * n2
	w[1] = fpow(G, (MOD - 1) // n)
	if inv:
		w[1] = fpow(w[1], MOD - 2)
	for i in range(2, n2):
		w[i] = mod_prod(w[i - 1], w[1])
	rev = [0] * n
	for i in range(n):
		rev[i] = rev[i >> 1] >> 1
		if i & 1:
			rev[i] |= n2
		if i < rev[i]:
			(a[i], a[rev[i]]) = (a[rev[i]], a[i])
	l = 2
	while l <= n:
		(half, diff) = (l // 2, n // l)
		for i in range(0, n, l):
			pw = 0
			for j in range(i, i + half):
				v = mod_prod(a[j + half], w[pw])
				a[j + half] = a[j] - v if a[j] - v >= 0 else a[j] - v + MOD
				a[j] = a[j] + v if a[j] + v < MOD else a[j] + v - MOD
				pw += diff
		l *= 2
	if inv:
		inv_n = fpow(n, MOD - 2)
		for i in range(n):
			a[i] = mod_prod(a[i], inv_n)
ntt_transform(f, 3)
f = [fpow(x, n // 2) for x in f]
ntt_transform(f, 3, inv=True)
ans = sum((mod_prod(x, x) for x in f)) % MODF
print(int(ans))
