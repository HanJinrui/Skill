r = int(input().split()[0])
x = y = 0
for i in range(r):
	a = input()
	for (j, v) in enumerate(a):
		if v == '*':
			x ^= j
			y ^= i
print(y + 1, x + 1)
