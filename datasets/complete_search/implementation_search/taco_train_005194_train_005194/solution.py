for _ in range(int(input())):
	(x, y) = map(int, input().split())
	m = 0
	for i in range(x):
		(w, h, p) = map(int, input().split())
		if y >= p:
			m = max(m, w * h)
	if m == 0:
		print('no tablet')
	else:
		print(m)
