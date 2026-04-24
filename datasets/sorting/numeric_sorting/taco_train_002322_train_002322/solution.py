n = 2 ** 20
a = [1] * n
r = {4}
for i in range(2, n):
	if a[i]:
		for j in range(i * i, n, i):
			a[j] = 0
		r.add(i * i)
input()
for d in map(int, input().split()):
	print(['NO', 'YES'][d in r])
