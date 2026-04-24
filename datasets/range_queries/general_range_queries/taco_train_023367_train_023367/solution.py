for xaxa in range(int(input())):
	o = 0
	m = 0
	s = input()
	n = len(s)
	for i in range(n):
		c = s[i]
		if c == '1':
			o += 1
		else:
			m += o
			if i < n - 1 and s[i + 1] == '1':
				m += o
	if s[-1] == '0':
		m += o
	print(m)
