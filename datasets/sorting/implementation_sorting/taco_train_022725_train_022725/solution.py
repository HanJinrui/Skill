a = sorted([[*map(int, s.split()), i] for (i, s) in enumerate([*open(0)][1:])], key=lambda x: (x[0], -x[1]))
print([a[0][2] + 1, -1][any((a[0][1] < x[1] for x in a))])
