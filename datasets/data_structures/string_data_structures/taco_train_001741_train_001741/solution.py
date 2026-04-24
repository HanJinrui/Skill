for _ in range(int(input())):
	r = ''
	a = input()
	b = input()
	for i in range(5):
		if a[i] == b[i]:
			r += 'G'
		else:
			r += 'B'
	print(r)
