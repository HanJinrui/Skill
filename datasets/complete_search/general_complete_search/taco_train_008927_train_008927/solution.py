(x, y) = (input(), input())
t = [0] * len(x)
p = {i: [] for i in 'abcdefghijklmnopqrstuvwxyz'}
for (i, j) in enumerate(x):
	p[j].append(i)
for i in y:
	for j in p[i]:
		t[j] += 1
	t = [0] + t
print(len(y) - max(t))
