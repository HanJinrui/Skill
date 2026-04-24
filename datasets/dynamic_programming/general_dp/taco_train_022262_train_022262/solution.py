M = 10 ** 9 + 7
s = 0
t = 0
for (i, c) in enumerate(map(int, input())):
	s = (10 * s + c * (i + 1)) % M
	t += s
print(t % M)
