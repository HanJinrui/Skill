(k, s) = (0, [])
for q in input():
	i = '[{<(]}>)'.find(q)
	if i > 3:
		if not s:
			s = 1
			break
		if s.pop() != i - 4:
			k += 1
	else:
		s += [i]
print('Impossible' if s else k)
