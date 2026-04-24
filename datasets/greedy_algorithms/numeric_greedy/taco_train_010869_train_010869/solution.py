from bisect import bisect

def main():
	input()
	l = sorted(((a, i) for (i, a) in enumerate(map(int, input().split()), 1)))
	(i, j) = (bisect(l, (0, -1)), bisect(l, (1, -1)))
	l = [i for (_, i) in l]
	(nn, zz, pp) = (l[:i], l[i:j], l[j:])
	(r, t) = ([], 0)
	if zz:
		t = zz.pop()
		for a in zz:
			r.append(f'1 {a} {t}')
	if len(nn) & 1:
		if t:
			r.append(f'1 {nn.pop()} {t}')
		else:
			t = nn.pop()
	nn += pp
	if nn:
		if t:
			r.append(f'2 {t}')
		t = nn.pop()
		for a in nn:
			r.append(f'1 {a} {t}')
	print('\n'.join(r))
main()
