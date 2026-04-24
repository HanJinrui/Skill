(a, b) = [*open(0)][1:]
if '*' in a:
	(x, y) = a.split('*')
	r = b.startswith(x) and b[len(x):].endswith(y)
else:
	r = a == b
print('NYOE S'[r::2])
