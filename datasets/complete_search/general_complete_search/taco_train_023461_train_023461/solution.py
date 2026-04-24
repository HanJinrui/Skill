I = lambda : map(int, input().split())
(n, m) = I()
A = list(I())
C = set()
for i in range(m):
	(x, y) = sorted(I())
	C.add((x - 1, y - 1))
print(min((A[i] + A[j] + A[k] for i in range(n) for j in range(i) for k in range(j) if {(j, i), (k, i), (k, j)} <= C), default=-1))
