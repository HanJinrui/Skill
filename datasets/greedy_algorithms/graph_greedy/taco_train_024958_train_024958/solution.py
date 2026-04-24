(n, y) = map(int, input().split())
q = list(map(int, input().split()))
(v, m, ans, j) = ([], {}, 0, 0)
for i in q:
	m[i] = 0
while len(v) != y:
	x = q[j]
	if m[x]:
		ans += m[x]
		v.append(x)
	if x + 1 not in m:
		m[x + 1] = m[x] + 1
		q.append(x + 1)
	if x - 1 not in m:
		m[x - 1] = m[x] + 1
		q.append(x - 1)
	j += 1
print(ans, '\n', *v)
