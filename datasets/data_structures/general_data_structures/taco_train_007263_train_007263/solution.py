l = []
for t in range(int(input())):
	s = input().split()
	if s[0] != '-1':
		p = int(s[0])
		b = s[1]
		if p != 0:
			k = [0, b, p]
			if len(l) == 0:
				l.append(k)
			elif p > l[-1][2]:
				l[-1][0] += 1
			else:
				l.append(k)
	else:
		(c, b, p) = l.pop()
		print(c, b)
