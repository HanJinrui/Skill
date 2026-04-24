s = input()
c = 'CODEFORCES'
print('NYOE S'[any((s.startswith(c[:i]) and s.endswith(c[i:]) for i in range(11)))::2])
