import io, os
ns = iter(os.read(0, os.fstat(0).st_size).split()).__next__
MX = 10 ** 6
MOD = 998244353
(n, m) = (int(ns()), int(ns()))
a = [int(ns()) for i in range(n * m)]
s = (int(ns()) - 1) * m + int(ns()) - 1
inv = [1] * MX
for i in range(2, MX):
	inv[i] = -(MOD // i) * inv[MOD % i] % MOD
ind = sorted(list(range(n * m)), key=lambda i: a[i])
fsum = isum = i2sum = jsum = j2sum = cnt = done = i = 0
while i < n * m:
	j = i
	tmpf = 0
	while j < n * m and a[ind[i]] == a[ind[j]]:
		(x, y) = divmod(ind[j], m)
		f = (fsum + cnt * (x * x + y * y) + i2sum + j2sum - 2 * (x * isum + y * jsum)) * inv[cnt] % MOD
		if ind[j] == s:
			done = 1
			break
		tmpf += f
		j += 1
	if done:
		break
	for k in range(i, j):
		(x, y) = divmod(ind[k], m)
		isum += x
		i2sum += x * x
		jsum += y
		j2sum += y * y
	fsum = (fsum + tmpf) % MOD
	cnt += j - i
	i = j
print(f)
