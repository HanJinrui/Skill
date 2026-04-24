(a, b, c) = map(int, input().split())
print(max(a * c * (c + 1) // 2 - b, 0))
