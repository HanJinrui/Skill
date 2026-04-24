input()
s = set()
t = (s.add, s.remove)
for c in input().split():
	t[c in s](c)
print(('Agasa', 'Conan')[bool(s)])
