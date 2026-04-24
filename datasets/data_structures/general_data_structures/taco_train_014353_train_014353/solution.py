N = 151
MOD = 10 ** 9 + 9
bt = [1]
oe = [{}]
for i in range(1, N):
	c = 0
	d = {}
	for j in range(i):
		l = bt[j]
		r = bt[i - j - 1]
		for (k, (e, o)) in oe[j].items():
			(de, do) = d.get(k, [0, 0])
			d[k] = [(de + o * r) % MOD, (do + e * r) % MOD]
		for (k, (e, o)) in oe[i - j - 1].items():
			(de, do) = d.get(k + j + 1, [0, 0])
			d[k + j + 1] = [(de + o * l) % MOD, (do + e * l) % MOD]
		(de, do) = d.get(j, [0, 0])
		d[j] = [(de + l * r) % MOD, do]
		c += l * r % MOD
	bt.append(c % MOD)
	oe.append(d)
for _ in range(int(input())):
	d = oe[int(input())]
	(a, b) = map(int, input().split())
	l = sorted(map(int, input().split()))
	e = o = 0
	for (k, (de, do)) in d.items():
		e += de * l[k] % MOD
		o += do * l[k] % MOD
	e %= MOD
	o %= MOD
	print((e * a % MOD + (MOD - o * b % MOD)) % MOD)
