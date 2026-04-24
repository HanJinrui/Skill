a = lambda : map(int, input().split())
(d, e, f) = a()
print(min((abs(i - e) for (i, z) in enumerate(a(), 1) if 0 < z <= f)) * 10)
