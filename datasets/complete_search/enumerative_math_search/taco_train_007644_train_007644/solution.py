n = input()
s = int(int(n) ** 0.5)
while s:
	r = str(s * s)
	c = 0
	for i in range(len(n)):
		if n[i] == r[c]:
			c += 1
			if c == len(r):
				exit(print(len(n) - c))
	s -= 1
print(-1)
