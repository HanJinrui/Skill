import sys
next((f := sys.stdin))
for (k, s) in zip(f, f):
	k = int(k.split()[1])
	r = 2 * s.count('10', 0, k) + (s[0] == '0')
	t = r - (s[k - 1] == '0')
	for (u, v, x, y) in zip(s, s[1:], s[k - 1:], s[k:-1]):
		t += (x != y) - (u != v)
		r = min(r, t + (y == '0'))
	print(r)
