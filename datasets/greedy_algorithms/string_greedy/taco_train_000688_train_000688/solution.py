def pow(x, exp, mod):
	res = 1
	while exp:
		if exp & 1:
			res = res * x % mod
		x = x * x % mod
		exp >>= 1
	return res
MOD = 2 ** 121 - 1
M = int(1000000000.0) + 1
n = int(input())
vals = list(map(int, input().split()))
groups = dict()
for i in range(n):
	groups.setdefault(vals[i], []).append(i)
powsA = [1]
for i in range(n):
	powsA.append(powsA[-1] * M % MOD)
hashes = [0] * (n + 1)
for i in range(n):
	hashes[i + 1] = (hashes[i] * M + vals[i]) % MOD

def get_hash(p, l):
	res = hashes[p + l] - hashes[p] * powsA[l] % MOD
	if res < 0:
		res += MOD
	elif res > MOD:
		res -= MOD
	return res
best = 0
i = 0
while i < n:
	val = vals[i]
	for j in groups[val]:
		if j <= i:
			continue
		l = j - i
		if j + l <= n and get_hash(i, l) == get_hash(j, l):
			best = max(best, j)
			i = j - 1
			break
	i += 1
res = vals[best:]
print(len(res))
print(' '.join(map(str, res)))
