n = int(input().split()[0])
a = sorted(map(int, input().split()))
print(min((y - x for (x, y) in zip(a, a[n - 1:]))))
