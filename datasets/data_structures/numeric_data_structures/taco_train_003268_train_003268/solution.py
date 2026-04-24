(n, m) = map(int, input().split())
print(*((m + 1) // 2 + (1 - 2 * ((m - 1 + i % m) % 2)) * ((1 + i % m) // 2) for i in range(n)), sep='\n')
