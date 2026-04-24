(n, s) = (int(input()), input())
print(sum((i.count('L') == i.count('R') and i.count('D') == i.count('U') for i in [s[x:y + 1] for x in range(n) for y in range(x, n)])))
