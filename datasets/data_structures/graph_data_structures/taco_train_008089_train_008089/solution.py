import sys
input = sys.stdin.readline
I = lambda : int(input())
A = lambda : [*map(int, input().split())]
mod = 10 ** 9 + 7
for _ in range(I()):
	n = I()
	(a, b, c) = (A(), A(), A())
	g = {a[i]: [b[i], c[i]] for i in range(n)}
	(cycles, visi) = (0, [False] * (n + 1))
	for u in range(1, n + 1):
		need = True
		cycle_size = 0
		while not visi[g[u][0]]:
			if g[u][1] != 0:
				need = False
			(visi[g[u][0]], u) = (True, g[u][0])
			cycle_size += 1
		if need and cycle_size > 1:
			cycles += 1
	print(pow(2, cycles, mod))
