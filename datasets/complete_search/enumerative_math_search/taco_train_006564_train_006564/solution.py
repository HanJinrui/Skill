input()
print(max(set(map(int, input().split())) - set([i ** 2 for i in range(1001)])))
