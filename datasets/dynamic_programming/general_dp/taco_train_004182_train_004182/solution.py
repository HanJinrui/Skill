mx = 10 ** 6
b = [None, None]
for n in range(2, mx * 2 + 1):
	a = [0, 0]
	while n > 0:
		d = n % 10
		a[d % 2] += d
		n = n // 10
	b.append(abs(a[0] - a[1]))
r = [None, 2, 12]
addend = 10
for n in range(3, mx + 1):
	addend -= 2 * b[n]
	addend += b[2 * n] + 2 * b[2 * n - 1] + b[2 * n - 2]
	r.append(r[-1] + addend)
for t in range(int(input())):
	print(r[int(input())])
