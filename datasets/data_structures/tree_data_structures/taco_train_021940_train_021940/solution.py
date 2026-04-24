import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = []
for _ in range(m):
	(l, r, q) = map(int, input().split())
	l -= 1
	r -= 1
	a.append((l, r, q))
res = [0] * n
bad = False
for i in range(30):
	events = [0] * (n + 1)
	for (l, r, q) in a:
		if q & 1 << i:
			events[l] += 1
			events[r + 1] -= 1
	c = 0
	for j in range(n):
		c += events[j]
		if c > 0:
			res[j] |= 1 << i
	s = [0] * (n + 1)
	for j in range(n):
		s[j + 1] = s[j] + (res[j] >> i & 1)
	for (l, r, q) in a:
		if q & 1 << i == 0:
			if s[r + 1] - s[l] == r - l + 1:
				bad = True
				break
if bad:
	print('NO')
else:
	print('YES')
	print(*res)
