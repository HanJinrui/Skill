def pprint(d):
	for row in d:
		print(*row[1:])
T = int(input())
for T in range(T):
	n = int(input())
	a = input()
	b = input()
	aa = [0]
	bb = [0]
	acount = 0
	bcount = 0
	for i in range(n):
		if a[i] == '1':
			acount += 1
		if b[i] == '1':
			bcount += 1
		aa.append(acount)
		bb.append(bcount)
	d = [[n * n for i in range(n + 1)] for i in range(n + 1)]
	d[1][0] = 0
	for row in range(1, n + 1):
		for col in range(1, n + 1):
			vara = d[row][col - 1]
			if a[col - 1] == '0':
				vara += bb[row - 1] + aa[col]
			varb = d[row - 1][col]
			if b[row - 1] == '0':
				varb += bb[row] + aa[col - 1]
			d[row][col] = min(vara, varb)
	print(d[n][n])
