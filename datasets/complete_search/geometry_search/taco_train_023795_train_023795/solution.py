a = list(map(int, input().split()))
print(sum(a[:3]) ** 2 - sum([p ** 2 for p in a[::2]]))
