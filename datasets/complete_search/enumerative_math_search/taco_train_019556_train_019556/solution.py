n = int(input())
print(sum((n // (i * i + j * j) for i in range(2, int(n ** 0.5) + 1) for j in range(1 + i % 2, i, 2) if __import__('math').gcd(i, j) < 2)))
