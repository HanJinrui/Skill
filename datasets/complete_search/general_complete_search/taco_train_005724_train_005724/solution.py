(n, m, k) = map(int, input().split())
x = dict()
val = n * m
for i in range(k):
	(r, c1, c2) = map(int, input().split())
	if r not in x:
		x[r] = (c1, c2)
	else:
		if x[r][1] < c1:
			val += c1 - x[r][1] - 1
		elif x[r][0] > c2:
			val += x[r][0] - c2 - 1
		x[r] = (min(x[r][0], c1), max(x[r][1], c2))
for t in x.values():
	val -= t[1] - t[0] + 1
print(val)
