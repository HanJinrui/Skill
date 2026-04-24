a = int(1000000000.0 + 7)
for _ in range(int(input())):
	n = int(input())
	x = list(map(int, input().split()))
	d = [[0] * 7 for _ in range(n + 1)]
	d[0][0] = 1
	for j in range(n):
		p = 10 ** len(str(x[j]))
		for l in range(7):
			w = (l * p + x[j]) % 7
			d[j + 1][l] = (d[j + 1][l] + d[j][l]) % a
			d[j + 1][w] = (d[j + 1][w] + d[j][l]) % a
	print((d[-1][0] - 1 + a) % a)
