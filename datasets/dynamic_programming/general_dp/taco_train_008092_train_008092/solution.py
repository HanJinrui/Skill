from functools import lru_cache
mod = 10 ** 9 + 7

@lru_cache(maxsize=None)
def f(i, odds, evens, K, prev):
	if i >= n:
		return int(K == 1)
	if p[i] != 0:
		return f(i + 1, odds, evens, K - (prev != p[i] % 2), p[i] % 2) % mod
	ans = 0
	if evens > 0:
		ans += evens * f(i + 1, odds, evens - 1, K - (prev != 0), 0) % mod
	if odds > 0:
		ans += odds * f(i + 1, odds - 1, evens, K - (prev != 1), 1) % mod
	return ans % mod
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	p = list(map(int, input().split()))
	f.cache_clear()
	odds = (n + 1) // 2
	evens = n // 2
	for v in p:
		if v != 0:
			if v % 2:
				odds -= 1
			else:
				evens -= 1
	if p[0] != 0:
		print(f(1, odds, evens, k, p[0] % 2))
	else:
		ans = evens * f(1, odds, evens - 1, k, 0) % mod
		f.cache_clear()
		ans = ans + odds * f(1, odds - 1, evens, k, 1) % mod
		print(ans % mod)
