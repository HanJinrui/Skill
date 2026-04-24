n = int(input())
l = []
for i in range(n):
	l.append(int(input()))
a = set(l)
if len(a) == 1:
	print('Exemplary pages.')
else:
	m = min(l)
	n = max(l)
	r = (n - m) // 2
	q = l.index(n)
	w = l.index(m)
	l[q] -= r
	l[w] += r
	b = set(l)
	if len(b) == 1:
		print(str(r) + ' ml. from cup #' + str(w + 1) + ' to cup #' + str(q + 1) + '.')
	else:
		print('Unrecoverable configuration.')
