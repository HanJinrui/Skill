l = [*map(int, open(0).read().split())]
n = l[0]
o = l[1:]
print(sum(o) - min(o[n - 1:-1:n - 1]))
