(a, b) = map(int, input().split())
d = [len(input()) for x in range(a)]
d.sort()
c = len(input())
i = d.index(c)
r = i + d.count(c)
print(i + 1 + i // b * 5, r + (r - 1) // b * 5)
