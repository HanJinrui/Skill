n = int(input())
print(*range(2, n // 2 + 1 + n % 2), 1, *range(n // 2 + 2 + n % 2, n + 1), n // 2 + 1 + n % 2, '\r' + str(n), *range(1, n))
