input()
L = [int(x) % 2 for x in input().split()]
print(L.index(sum(L) == 1) + 1)
