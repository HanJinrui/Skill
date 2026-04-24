(a, b, c, d) = sorted(map(int, input().split()))
print(('YES', 'NO')[a - c + d != b != d - a - c])
