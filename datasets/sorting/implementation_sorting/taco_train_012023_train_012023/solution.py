a = sorted({*map(int, [*open(0)][1].split())})
print('YNEOS'[len(a) == 3 and a[1] - a[0] != a[2] - a[1] or len(a) > 3::2])
