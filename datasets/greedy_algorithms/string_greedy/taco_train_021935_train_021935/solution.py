n = int(input())
s = input()
l = sorted(((abs(n / 2 - i), i) for i in range(1, n) if s[i] != '0'))
print(min((int(s[:i]) + int(s[i:]) for (v, i) in l[:2])))
