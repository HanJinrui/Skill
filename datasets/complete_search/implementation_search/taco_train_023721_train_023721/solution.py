a = input()
(x, y) = [a.count(x) for x in '47']
print([[4, 7][y > x], -1][x < 1 > y])
