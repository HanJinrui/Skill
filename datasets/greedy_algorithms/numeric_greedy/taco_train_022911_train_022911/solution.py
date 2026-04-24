R = lambda : map(int, input().split())
(n, m) = R()
(a, b) = [sum((x % 2 for x in R())) for _ in range(2)]
print(min(a, m - b) + min(n - a, b))
