raw = input()
s = raw.replace('?', '')
n = int(s.split()[-1])
m = s.count('-')
p = s.count('+')
c = p - m
if (p + 1) * n - m < n or p + 1 - m * n > n:
	print('Impossible')
else:
	print('Possible')
	rez = n - c
	s = raw[1:]
	while rez > n or rez < 1:
		if rez > n:
			s = s.replace('+ ?', '+ ' + str(n), 1)
			rez -= n - 1
		else:
			s = s.replace('- ?', '- ' + str(n), 1)
			rez += n - 1
	print(str(rez) + s.replace('?', '1'))
