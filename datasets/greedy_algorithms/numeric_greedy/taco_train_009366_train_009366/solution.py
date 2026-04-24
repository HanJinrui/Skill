n = int(input())
print('NYOE S'[n % 2::2], *(i % n * 2 + i % 2 + 1 for i in range(n % 2 * 2 * n)))
