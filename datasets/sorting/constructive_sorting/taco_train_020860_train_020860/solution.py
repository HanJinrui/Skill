(n, m) = map(int, input().split())
a = [0] + list(map(int, input().split()))
(p, t, k) = ([], [True] * (n + 1), n // m)
(u, v) = (10001, -1)
for i in range(int(input())):
	q = list(map(int, input().split()))
	if t[q[0]]:
		for i in q:
			t[i] = False
		x = sum((a[i] for i in q))
		if x < u:
			u = x
		if x > v:
			v = x
		m -= 1
q = sorted((a[i] for i in range(1, n + 1) if t[i]))
if len(q) >= k and m:
	(x, y) = (sum(q[:k]), sum(q[-k:]))
	if x < u:
		u = x
	if y > v:
		v = y
print(u / k, v / k)
