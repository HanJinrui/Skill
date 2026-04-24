s = input()
(c, h, e, f) = (0, 0, 0, 0)
for ch in s:
	if ch == 'C':
		c += 1
	elif ch == 'H':
		if c > h:
			h += 1
	elif ch == 'E':
		if h > e:
			e += 1
	elif e > f:
		f += 1
print(f)
