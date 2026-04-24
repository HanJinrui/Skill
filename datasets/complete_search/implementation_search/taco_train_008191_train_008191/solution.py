(x, y, z) = sorted((int(n) + 9 * ord(s) for (n, s) in input().split()))
D = {y - x, z - y}
print(2 - bool(D & {0, 1, 2}) - (D < {0, 1}))
