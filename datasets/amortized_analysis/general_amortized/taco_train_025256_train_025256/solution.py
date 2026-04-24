(n, s) = (int(input()), input() * 2)
h = s.count('H') // 2
print(h - max((s[i:i + h].count('H') for i in range(n))))
