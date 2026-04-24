(a, b) = open(0)
print([b, -1][any((y > x for (x, y) in zip(a, b)))])
