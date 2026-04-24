I = lambda : list(map(int, input().split()))
(n, l) = I()
a = I()
print(max((i * sum((x // i for x in a)) for i in range(l, 101))))
