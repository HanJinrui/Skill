(x, y) = map(int, input().split())
print(min(((lambda u, v, w: ((x - u) ** 2 + (y - v) ** 2) ** 0.5 / w)(*map(int, input().split())) for i in range(int(input())))))
