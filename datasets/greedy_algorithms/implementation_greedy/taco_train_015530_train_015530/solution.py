s = input()
try:
	i = s.index(':', s.index('['))
	r = s.count('|', i, s.rindex(':', i + 1, s.rindex(']', i))) + 4
except:
	r = -1
print(r)
