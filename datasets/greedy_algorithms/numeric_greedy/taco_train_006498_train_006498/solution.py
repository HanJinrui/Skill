t = int(input())
for i in range(t):
	n = int(input())
	p = list(map(int, input().split()))
	l = [p[0]]
	r = []
	for w in p[1:]:
		if w < l[-1]:
			l.append(w)
		else:
			r.append(w)
	print(*l[::-1] + r)
