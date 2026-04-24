(n, m) = map(int, input().split())
k = n // m
z = n - m
print(m * k * (k - 1) // 2 + k * (n % m), (z + 1) * z // 2)
