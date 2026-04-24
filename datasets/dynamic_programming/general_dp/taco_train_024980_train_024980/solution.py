import re
for _ in range(int(input())):
	a = input()
	b = ['[%s%s]' % (c, c.lower()) for c in input()]
	pattern = '^[a-z]*' + '[a-z]*'.join(b) + '[a-z]*$'
	print('YES' if re.match(pattern, a) else 'NO')
