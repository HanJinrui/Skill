from collections import defaultdict
(N, K) = map(int, input().split())

def check(n, p=None):
	c = 0
	e = [p == None, p != None] + [0] * (N - 2)
	for ch in T[n]:
		if ch == p:
			continue
		(C, E) = check(ch, n)
		c += C
		e2 = [0] * N
		for x in range(N - 1):
			for y in range(1, N - x):
				e2[x + y - 1] += e[x] * E[y]
			e2[x + 1] += e[x]
		e = e2
	c += sum(e[:K + 1])
	return (c, e)
T = defaultdict(list)
for _ in range(N - 1):
	(a, b) = map(int, input().split())
	T[a].append(b)
	T[b].append(a)
print(check(1)[0] + 1)
