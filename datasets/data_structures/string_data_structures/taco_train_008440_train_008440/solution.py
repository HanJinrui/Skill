s = [(0, 0)]
c = 0
for (i, x) in enumerate(input()):
	c += -1 if x.lower() in 'aeiou' else 2
	s.append((c, i + 1))
lis = sorted(s)
u = 10 ** 9
d = {}
answer = 0
for i in lis:
	if u < i[1]:
		if i[1] - u >= answer:
			answer = i[1] - u
			d[answer] = d.get(answer, 0) + 1
	else:
		u = min(u, i[1])
if answer != 0:
	print(answer, d[answer])
else:
	print('No solution')
