s = input().split('@')
if len(s) > 1 and s[0] and s[-1] and (min(map(len, s[1:-1] + ['__'])) > 1):
	for i in range(1, len(s) - 1):
		s[i] = s[i][0] + ',' + s[i][1:]
	print('@'.join(s))
else:
	print('No solution')
