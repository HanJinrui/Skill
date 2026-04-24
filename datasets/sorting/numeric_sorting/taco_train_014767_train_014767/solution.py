n = int(input())
a = sorted(map(int, input().split()))
print(a[-1] - a[0], (a.count(a[-1]) * a.count(a[0]), n * (n - 1) // 2)[a[-1] == a[0]])
