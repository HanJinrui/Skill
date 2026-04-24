((a, b), (c, d), (e, f), (g, h), (i, j), (k, l), (m, n), (o, p)) = sorted((tuple(map(int, input().split())) for _ in range(8)))
print(('ugly', 'respectable')[a == c == e < g == i < k == m == o and b == h == l < d == n < f == j == p])
