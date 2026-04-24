(n, m, k) = map(int, input().split())
print(max(0, n - m - min(k, input().count('2'))))
