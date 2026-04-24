lis = lambda : map(int, input().split())
(n, d) = lis()
a = [*lis()]
print(sum((abs(x - y) <= d for x in a for y in a)) - n)
