for _ in range(int(input())):
	n = int(input())
	s = input()
	if s.index('code') < s.index('chef'):
		print('AC')
	else:
		print('WA')
