from math import *
(n, vb, vs, d, xu, yu) = (*list(map(int, input().split())), list(map(int, input().split())), *list(map(int, input().split())))
print(min([(d[i] / vb + hypot(xu - d[i], yu) / vs, hypot(xu - d[i], yu), i + 1) for i in range(1, len(d))])[2])
