n = int(input())
print(['NO', '1 %d' % (n // 2 - 1)][n & 1 & (n > 3)])
