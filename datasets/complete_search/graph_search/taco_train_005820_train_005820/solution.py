import sys
input = sys.stdin.readline

def solve():
	(n, m) = map(int, input().split())
	p = list(map(int, input().split()))
	s = [0] * n
	for i in range(n):
		v = p[i] - 1
		s[(i - v) % n] += 1
	z = n - 2 * m
	r = []
	for i in range(n):
		if s[i] >= z:
			w = [True] * n
			c = 0
			for j in range(n):
				if w[j]:
					c += 1
					while w[j]:
						w[j] = False
						v = p[j] - 1
						j = (v + i) % n
			if n - c <= m:
				r.append(i)
	print(len(r), end=' ')
	print(' '.join(map(str, r)))
for i in range(int(input())):
	solve()
