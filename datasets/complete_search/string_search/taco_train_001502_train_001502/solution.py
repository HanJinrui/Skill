input()
s = input()
print(min((sum((min(x, 26 - x) for x in map(lambda x, y: abs(ord(x) - ord(y)), t, 'ACTG'))) for t in zip(s, s[1:], s[2:], s[3:]))))
