n = int(input())
s = input().strip()
print('yes' if '*****' in '.'.join((s[i::j] for i in range(n) for j in range(1, n))) else 'no')
