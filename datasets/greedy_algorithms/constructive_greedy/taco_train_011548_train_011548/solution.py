(n, m) = map(int, input().split())
a = [input().split() for i in range(n)]
b = [*zip(*a)]
print([4, 2]['1' in ''.join([*a[0], *a[n - 1], *b[0], *b[m - 1]])])
