o = '{[('
c = '}])'
for _ in range(int(input())):
	s = []
	for e in input():
		if e in o:
			s.append(e)
		elif not len(s) or c[o.index(s.pop())] != e:
			print('NO')
			break
	else:
		if len(s):
			print('NO')
		else:
			print('YES')
