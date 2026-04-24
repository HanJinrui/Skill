(n, k) = map(int, input().split())
a = sorted(map(int, input().split()))
x = a[(k - 1) // n]
(p, c) = (a.index(x), a.count(x))
y = (k - 1 - p * n) // c
print(x, a[y])
