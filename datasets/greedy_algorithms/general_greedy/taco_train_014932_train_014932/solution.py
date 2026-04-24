input()
t = []
for (y, d) in enumerate(map(int, input().split()), 2001):
	if d == len(t) + 1:
		t.append(y)
print(len(t), *t)
