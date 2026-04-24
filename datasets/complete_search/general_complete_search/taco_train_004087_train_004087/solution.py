def Mx(M, x):
	return (M[0] * x[0] + M[1] * x[1] + M[2], M[3] * x[0] + M[4] * x[1] + M[5])

def MM(M, M2):
	return (M[0] * M2[0] + M[1] * M2[3], M[0] * M2[1] + M[1] * M2[4], M[0] * M2[2] + M[1] * M2[5] + M[2], M[3] * M2[0] + M[4] * M2[3], M[3] * M2[1] + M[4] * M2[4], M[3] * M2[2] + M[4] * M2[5] + M[5])
n = int(input())
squares = [(1, 1, n - 1)]
maps = [(1, 0, 0, 0, 1, 0)]
s = int(input())
for _ in range(s):
	(a, b, d) = map(int, input().split())
	squares.append((a, b, d))
	maps.append(MM((0, 1, a - b, -1, 0, a + b + d), maps[-1]))
assert len(squares) == len(maps) == s + 1
for _ in range(int(input())):
	w = int(input())
	y = x = (w // n + 1, w % n + 1)
	(lo, hi) = (0, s + 1)
	while lo + 1 < hi:
		mid = (lo + hi) // 2
		(a, b, d) = squares[mid]
		(r, c) = Mx(maps[mid], x)
		if a <= r <= a + d and b <= c <= b + d:
			lo = mid
			y = (r, c)
		else:
			hi = mid
	print(y[0], y[1])
