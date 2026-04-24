R = lambda : map(int, input().split())
(n, s) = R()
a = sorted(R())
m = n // 2
print(abs(a[m] - s) + sum((max(0, x - s) for x in a[:m])) + sum((max(0, s - x) for x in a[m + 1:])))
