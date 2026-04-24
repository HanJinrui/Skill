i = lambda : map(int, input().split())
(a, b, c) = i()
i()
print(sum((b < x < c for x in i())))
