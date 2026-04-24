d1 = {}

def solve1(fn, f, c, N, t):
	if N == 0 or N == c:
		return -1
	t2 = 1 if t == 2 else 2
	m = []
	if fn == 1:
		d1k = (f[0] - 1, c, N - 1, t2)
		if d1k in d1:
			m += d1[d1k]
		else:
			m += [solve1(1, [f[0] - 1], c, N - 1, t2)]
			d1[d1k] = m
	elif fn == 2:
		if f[0] > 0:
			m += [solve1(1, [f[0] + f[2] - 1], c + f[1], N - 1, t2)]
		if f[1] > 0:
			m += [solve1(1, [f[1] + f[2] - 1], c + f[0], N - 1, t2)]
		if f[2] > 0:
			m += [solve1(2, [f[0], f[1], f[2] - 1], c, N - 1, t2)]
	elif fn == 3:
		if f[0] > 0:
			m += [solve1(1, [f[0] + f[3] + f[4] + f[6] - 1], c + f[1] + f[2] + f[5], N - 1, t2)]
		if f[1] > 0:
			m += [solve1(1, [f[1] + f[3] + f[5] + f[6] - 1], c + f[0] + f[2] + f[4], N - 1, t2)]
		if f[2] > 0:
			m += [solve1(1, [f[2] + f[4] + f[5] + f[6] - 1], c + f[0] + f[1] + f[3], N - 1, t2)]
		if f[3] > 0:
			m += [solve1(2, [f[0] + f[4], f[1] + f[5], f[3] + f[6] - 1], c + f[2], N - 1, t2)]
		if f[4] > 0:
			m += [solve1(2, [f[0] + f[3], f[2] + f[5], f[4] + f[6] - 1], c + f[1], N - 1, t2)]
		if f[5] > 0:
			m += [solve1(2, [f[1] + f[3], f[2] + f[4], f[5] + f[6] - 1], c + f[0], N - 1, t2)]
		if f[6] > 0:
			m += [solve1(3, [f[0], f[1], f[2], f[3], f[4], f[5], f[6] - 1], c, N - 1, t2)]
	return 1 if -1 in m else -1
d2 = {}

def solve2(fn, f, c, N, p, t):
	if N == 0 or N == c:
		return p if t == 2 else 0
	r = 0
	if t == 2:
		r += p * c / N
	t2 = 1 if t == 2 else 2
	if fn == 1:
		d2k = (f[0] - 1, c, N - 1, p * f[0] / N, t2)
		if d2k in d2:
			r += d2[d2k]
		else:
			rt = solve2(1, [f[0] - 1], c, N - 1, p * f[0] / N, t2)
			d2[d2k] = rt
			r += rt
	elif fn == 2:
		if f[0] > 0:
			r += solve2(1, [f[0] + f[2] - 1], c + f[1], N - 1, p * f[0] / N, t2)
		if f[1] > 0:
			r += solve2(1, [f[1] + f[2] - 1], c + f[0], N - 1, p * f[1] / N, t2)
		if f[2] > 0:
			r += solve2(2, [f[0], f[1], f[2] - 1], c, N - 1, p * f[2] / N, t2)
	elif fn == 3:
		if f[0] > 0:
			r += solve2(1, [f[0] + f[3] + f[4] + f[6] - 1], c + f[1] + f[2] + f[5], N - 1, p * f[0] / N, t2)
		if f[1] > 0:
			r += solve2(1, [f[1] + f[3] + f[5] + f[6] - 1], c + f[0] + f[2] + f[4], N - 1, p * f[1] / N, t2)
		if f[2] > 0:
			r += solve2(1, [f[2] + f[4] + f[5] + f[6] - 1], c + f[0] + f[1] + f[3], N - 1, p * f[2] / N, t2)
		if f[3] > 0:
			r += solve2(2, [f[0] + f[4], f[1] + f[5], f[3] + f[6] - 1], c + f[2], N - 1, p * f[3] / N, t2)
		if f[4] > 0:
			r += solve2(2, [f[0] + f[3], f[2] + f[5], f[4] + f[6] - 1], c + f[1], N - 1, p * f[4] / N, t2)
		if f[5] > 0:
			r += solve2(2, [f[1] + f[3], f[2] + f[4], f[5] + f[6] - 1], c + f[0], N - 1, p * f[5] / N, t2)
		if f[6] > 0:
			r += solve2(3, [f[0], f[1], f[2], f[3], f[4], f[5], f[6] - 1], c, N - 1, p * f[6] / N, t2)
	return r

def main():
	prc = [0 for i in range(101)]
	for i in range(2, 101):
		if prc[i] == 1:
			continue
		for j in range(i + i, 101, i):
			prc[j] = 1
	prm = []
	for i in range(2, 101):
		if prc[i] == 0:
			prm += [i]
	fac = [[] for i in range(101)]
	for i in range(2, 101):
		for p in prm:
			if p > i:
				continue
			if i % p == 0:
				fac[i] += [p]
	T = int(input())
	while T > 0:
		N = int(input())
		inp = input().split(' ')
		a = [int(n) for n in inp]
		r1 = 0
		r2 = 0
		d1.clear()
		d2.clear()
		for i in range(N):
			x = a[i]
			if x == 1:
				continue
			fn = len(fac[x])
			f = [0 for j in range(2 ** fn - 1)]
			c = 0
			for j in range(N):
				if i == j:
					continue
				y = a[j]
				if fn == 3:
					if fac[x][0] in fac[y]:
						if fac[x][1] in fac[y]:
							if fac[x][2] in fac[y]:
								f[6] += 1
							else:
								f[3] += 1
						elif fac[x][2] in fac[y]:
							f[4] += 1
						else:
							f[0] += 1
					elif fac[x][1] in fac[y]:
						if fac[x][2] in fac[y]:
							f[5] += 1
						else:
							f[1] += 1
					elif fac[x][2] in fac[y]:
						f[2] += 1
					else:
						c += 1
				elif fn == 2:
					if fac[x][0] in fac[y]:
						if fac[x][1] in fac[y]:
							f[2] += 1
						else:
							f[0] += 1
					elif fac[x][1] in fac[y]:
						f[1] += 1
					else:
						c += 1
				elif fn == 1:
					if fac[x][0] in fac[y]:
						f[0] += 1
					else:
						c += 1
			if r1 == 0 and solve1(fn, f, c, N - 1, 2) == -1:
				r1 = 1
			r2 += solve2(fn, f, c, N - 1, 1 / N, 2)
		print('%d %.4f' % (r1, r2))
		T -= 1
main()
