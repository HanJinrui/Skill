k = lambda : map(int, input().split())
(_, x) = k()
print(x + sum(((i == x) - (i < x) for i in k())))
