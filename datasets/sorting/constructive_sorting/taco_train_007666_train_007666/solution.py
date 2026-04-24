input()
a = sorted(input().split(), key=int)
print(a[-1], *a[1:-1], a[0])
