a = [input().split() for _ in range(int(input()))]
print(sum((x[0] == y[1] for x in a for y in a)))
