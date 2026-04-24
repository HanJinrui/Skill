n = int(input())
x = n // 2 + 1
print([x ** 2, 2 * x * (x + 1)][n % 2])
