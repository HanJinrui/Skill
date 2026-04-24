n = int(input())
p = [[0, 0]]
l = [0]
v = []
for (i, c) in enumerate(map(int, input().split())):
	p.extend([[i + 1, j + 1] for j in range(c)])
	l.extend(list(map(int, input().split())))
for i in range(1, len(l)):
	if l[i] != i:
		j = l.index(i)
		v.append(p[i] + p[j])
		(l[i], l[j]) = (l[j], l[i])
print(len(v))
for x in v:
	print(' '.join(map(str, x)))
