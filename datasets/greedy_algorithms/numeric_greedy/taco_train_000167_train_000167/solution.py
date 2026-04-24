(x, y, z) = list(map(int, input().split()))
print((x + y) // z, max(min(x % z, y % z) - (x + y) % z, 0))
