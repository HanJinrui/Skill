n = int(input())
a = (sum((int(input().split()[1]) for _ in ' ' * n)) + 499) // 1000
print('A' * a + 'G' * (n - a))
