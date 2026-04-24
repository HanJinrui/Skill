I = lambda : map(int, input().split())
(n, m) = I()
A = [[*I()] for _ in range(n)]
(a, b) = I()
print(min((sum((A[i][j] for i in range(x, x + dx) for j in range(y, y + dy))) for (dx, dy) in ((a, b), (b, a)) for x in range(n - dx + 1) for y in range(m - dy + 1))))
