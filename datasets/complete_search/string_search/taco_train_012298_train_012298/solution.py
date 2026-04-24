from decimal import *
a = Decimal(input())
print([a, '%d' % a][int(a) == a])
