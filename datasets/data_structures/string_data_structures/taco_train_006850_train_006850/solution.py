t = int(input())
for _ in range(t):
	s = input()
	pos = s.find('W')
	print('Chef' if 2 * pos + 1 == len(s) else 'Aleksa')
