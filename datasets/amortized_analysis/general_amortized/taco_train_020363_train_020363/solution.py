L = lambda : [*map(int, input().split())]
(r, c, n, k) = L()
A = [L() for _ in range(n)]
print(sum((sum((a <= x <= b and f <= y <= g for (x, y) in A)) >= k for a in range(1, r + 1) for b in range(a, r + 1) for f in range(1, c + 1) for g in range(f, c + 1))))
