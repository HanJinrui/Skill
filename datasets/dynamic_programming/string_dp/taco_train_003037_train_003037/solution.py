(n, l) = (int(input()), [(0, '')])
for i in map(int, input().split()):
	s = input()
	l = sorted(((x + y, b) for (y, b) in ((0, s), (i, s[::-1])) for (x, a) in l if a <= b))
	for i in range(len(l) - 1, 0, -1):
		for j in range(i):
			if l[i][1] >= l[j][1]:
				del l[i]
				break
print(min(l)[0] if l else -1)
