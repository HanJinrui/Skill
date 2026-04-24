def onedsum(a):
	ds = 0
	while a > 9:
		(a, u) = divmod(a, 10)
		ds += u
	return ds + a

def rangetodsum(lo, hi):
	(lod, lom) = divmod(lo, 10)
	(hid, him) = divmod(hi, 10)
	if lod == hid:
		dlo = onedsum(lod)
		dsum = {dlo + i: 1 for i in range(lom, him + 1)}
	else:
		dlo = onedsum(lod)
		dsum = {dlo + i: 1 for i in range(lom, 10)}
		dhi = onedsum(hid)
		for h in range(dhi, dhi + him + 1):
			if h in dsum:
				dsum[h] += 1
			else:
				dsum[h] = 1
		lod += 1
		hid -= 1
		if lod <= hid:
			rsum = rangetodsum(lod, hid)
			for r in rsum:
				for u in range(10):
					k = r + u
					if k in dsum:
						dsum[k] += rsum[r]
					else:
						dsum[k] = rsum[r]
	return dsum
mdl = 1000000007
for _ in range(int(input())):
	(l, r) = map(int, input().split())
	dsum = rangetodsum(l, r)
	dlst = list(dsum.items())
	awk = 0
	if 1 in dsum:
		awk = dsum[1] * (dsum[1] - 1) // 2
	for ix1 in range(len(dlst) - 1):
		a = dlst[ix1]
		for ix2 in range(ix1 + 1, len(dlst)):
			b = dlst[ix2]
			(f, g) = (a[0], b[0])
			while f > 0:
				(g, f) = (f, g % f)
			if g == 1:
				awk += a[1] * b[1]
				awk %= mdl
	print(awk)
