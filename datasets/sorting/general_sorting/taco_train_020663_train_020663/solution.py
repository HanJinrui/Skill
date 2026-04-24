input()
b = input().split()
print(max(map(b.count, b)), len(set(b)))
