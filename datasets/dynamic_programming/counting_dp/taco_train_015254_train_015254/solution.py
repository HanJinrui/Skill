p = [[0] * 2527 for i in range(101)]
p[0][0] = 1
for n in range(100):
	for s in range(2501):
		p[n + 1][s] = (p[n + 1][s - 1] + p[n][s] - p[n][s - 26]) % 1000000007
for j in range(int(input())):
	t = input()
	s = sum((ord(q) - 97 for q in t))
	print(p[len(t)][s] - 1)
