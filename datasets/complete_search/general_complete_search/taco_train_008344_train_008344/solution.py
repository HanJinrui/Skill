a = [[*map(int, s.split())] for s in [*open(0)][1:]]
print('YNEOS'[all((u + v != w or w + x != u for (u, v) in a for (w, x) in a))::2])
