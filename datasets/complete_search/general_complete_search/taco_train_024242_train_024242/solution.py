input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min((max((x * y for x in a[:i] + a[i + 1:] for y in b)) for i in range(len(a)))))
