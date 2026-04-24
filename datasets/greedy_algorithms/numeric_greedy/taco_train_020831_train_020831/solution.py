input()
print(sum((i * x - i + x for (i, x) in enumerate(map(int, input().split())))))
