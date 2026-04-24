a = int(input())
x = a - 10 ** 21 * 9 % a
print(x, 10 ** 20 + x - 1)
