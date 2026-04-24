for _ in range(int(input())):
	count = [0] * (2 * int(input()) + 1)
	f = [0] * 3
	u = 0
	count[u] += 1
	f[u % 3] += 1
	total = 0
	for x in input():
		if x == '-':
			u -= 1
			f[u % 3] += count[u]
		else:
			f[u % 3] -= count[u]
			u += 1
		total += f[u % 3]
		count[u] += 1
		f[u % 3] += 1
	print(total)
