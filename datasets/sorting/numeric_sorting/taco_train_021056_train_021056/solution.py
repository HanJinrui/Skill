S = int(input())
v = [int(x) for x in input().strip().split()]
print(*([S * v[i] / sum(v) for i in range(3)] if sum(v) != 0 else '000'))
