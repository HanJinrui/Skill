input()
a = p = c = o = 0
for i in input():
	if i == 'G':
		c += 1
		a += 1
	else:
		p = c
		c = 0
	o = max(o, p + c + 1)
print(min(o, a))
