s = set()
r = f = 1
for c in input():
	if c == '?':
		r *= [10, 9][f]
	elif c.isalpha():
		if c not in s:
			r *= [10, 9][f] - len(s)
			s |= {c}
	f = 0
print(r)
