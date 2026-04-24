(n, m) = map(int, input().split())
print(*[[max(m, n), [n, m + n - 1][m > 0]], ['Impossible']][n == 0 and m > 0])
