a = [() for _ in [0] * int(input())]
i = 0
for x in map(int, input().split()):
	a[x - 1] += (i,)
	i += 1
print(sum((abs(y - x) for t in zip(*a) for (x, y) in zip((0,) + t, t))))
