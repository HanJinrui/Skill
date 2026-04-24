input()
a = [*map(int, input().split())]
(c, t) = min(((sum((max(0, abs(t - x) - 1) for x in a)), t) for t in range(1, max(a) + 1)))
print(t, c)
