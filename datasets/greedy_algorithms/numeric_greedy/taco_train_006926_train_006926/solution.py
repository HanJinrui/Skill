raw = input()
s = raw.replace('?', '')
n = int(s.split(' ')[-1])
m = s.count('-')
p = s.count('+')
c = p - m
if (p + 1) * n - m < n or p + 1 - m * n > n:
	print('Impossible')
else:
	print('Possible')
	acc = n - c
	s = raw[1:]
	while acc > n or acc < 1:
		if acc > n:
			s = s.replace('+ ?', '+ ' + str(n), 1)
			acc -= n - 1
		else:
			s = s.replace('- ?', '- ' + str(n), 1)
			acc += n - 1
	print(str(acc) + s.replace('?', '1'))
