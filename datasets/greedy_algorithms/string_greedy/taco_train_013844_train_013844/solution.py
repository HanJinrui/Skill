import re
p = ('[a-z]', '[A-Z]', '[0-9]')
for _ in [0] * int(input()):
	s = input()
	for x in p:
		for y in p:
			if not re.search(f'{x}', s):
				s = re.sub(f'({y})(.*{y})', f'{x[1]}\\2', s)
	print(s)
