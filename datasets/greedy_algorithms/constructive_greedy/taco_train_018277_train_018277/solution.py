d = lambda x: abs(int(x ** 0.5 + 0.5) ** 2 - x)
n = int(input()) // 2
a = sorted([[d(int(x)), int(x)] for x in input().split()])
print(sum((i[0] for i in a[:n])) + sum(((i[0] == 0) + (i[1] == 0) for i in a[n:])))
