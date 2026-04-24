(n, d) = map(int, input().split())
a = input().split()
print(*a[d:] + a[:d])
