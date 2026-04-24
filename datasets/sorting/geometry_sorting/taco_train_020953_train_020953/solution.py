d = list(map(int, input().split()))
(V, T) = map(int, input().split())
v = tuple(map(int, input().split()))
w = tuple(map(int, input().split()))
o = d[0:2]
d = d[2:4]
(l, r) = (0, 1000000000)
for i in range(300):
	(m, e) = ((l + r) / 2, o[:])
	if m <= T:
		e[0] += m * v[0]
		e[1] += m * v[1]
	else:
		e[0] += T * v[0]
		e[1] += T * v[1]
		e[0] += (m - T) * w[0]
		e[1] += (m - T) * w[1]
	if (d[0] - e[0]) * (d[0] - e[0]) + (d[1] - e[1]) * (d[1] - e[1]) <= V * V * m * m:
		a = m
		r = m - 1e-06
	else:
		l = m + 1e-06
print(a)
