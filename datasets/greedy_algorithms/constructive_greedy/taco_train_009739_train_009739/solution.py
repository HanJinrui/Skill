n = int(input())
q = int(0.5 + (1 + 8 * n) ** 0.5 / 2)
w = 1
qw = [[] for _ in range(q)]
for i in range(q):
	j = i + 1
	while len(qw[i]) < q - 1:
		qw[i].append(str(w))
		qw[j].append(str(w))
		w = w + 1
		j = j + 1
print(q)
for q in qw:
	print(' '.join(q))
