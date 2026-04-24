f = lambda : map(int, input().split())
print(2 * sum((max(1, abs(a - b)) + 1 for (a, b) in zip(f(), f()))))
