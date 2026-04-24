(a, b) = map(int, input().split())
print('NYOE S'[(abs(a - b) < 2) * (a + b > 0)::2])
