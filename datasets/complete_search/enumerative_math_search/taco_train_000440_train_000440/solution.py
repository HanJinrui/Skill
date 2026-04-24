n = int(input())
li = [x for x in range(max(1, n - 99), n) if x + sum(map(int, str(x))) == n]
print(len(li))
print(*li)
