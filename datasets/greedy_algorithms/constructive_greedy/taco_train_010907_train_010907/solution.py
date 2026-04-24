import collections
t = int(input())
for _ in range(t):
	s = input()
	r = collections.Counter(input())
	r.subtract(s)
	if any((v < 0 for v in r.values())):
		print('Impossible')
	else:
		r = [*r.elements(), s]
		r.sort(key=lambda x: x[0] + (x.lstrip(x[0]) or x)[0])
		print(''.join(r))
