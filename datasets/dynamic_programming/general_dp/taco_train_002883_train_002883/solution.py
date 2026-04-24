for i in range(int(input())):
	input()
	l = list(map(int, input().split()))
	r1 = sum(filter(lambda x: x > 0, l))
	if r1 <= 0:
		r1 = max(l)
	r2 = 0
	t = 0
	for j in l:
		t += j
		t = max(0, t)
		r2 = max(r2, t)
	if r2 <= 0:
		r2 = max(l)
	print('%i %i' % (r2, r1))
