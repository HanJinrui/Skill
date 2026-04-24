import math

def dis(x1, y1, x2, y2):
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def ted(f, s, l, x, y):
	mn = 10000000000
	m1 = 10000000000
	m2 = 10000000000
	m3 = 10000000000
	for i in range(0, len(f), 2):
		m1 = dis(x, y, f[i], f[i + 1])
		if m1 > mn:
			continue
		for j in range(0, len(s), 2):
			m2 = m1 + dis(f[i], f[i + 1], s[j], s[j + 1])
			if m2 > mn:
				continue
			for k in range(0, len(l), 2):
				m3 = m2 + dis(s[j], s[j + 1], l[k], l[k + 1])
				if m3 < mn:
					mn = m3
	return mn
t = int(input())
for ts in range(t):
	(x, y) = map(int, input().split())
	(n, m, k) = map(int, input().split())
	ln = list(map(int, input().split()))
	lm = list(map(int, input().split()))
	lk = list(map(int, input().split()))
	a = ted(ln, lm, lk, x, y)
	b = ted(lm, ln, lk, x, y)
	print(min(a, b))
