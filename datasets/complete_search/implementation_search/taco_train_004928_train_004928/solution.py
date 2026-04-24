i = lambda : list(map(int, input().split()))
i()
a = i()
i()
b = i()
l = [x // y for x in b for y in a if x % y == 0]
print(l.count(max(l)))
